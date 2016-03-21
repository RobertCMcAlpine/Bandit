from django.shortcuts import render
from bandit.forms import UserForm, ProfileForm, EventForm, BandForm, VenueForm, EditProfileForm
from bandit.models import Profile, Band, Venue, Event, Request, Image
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from datetime import date,time


def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    
    # Render the response and send it back!
    return render(request, 'bandit/index.html')


def register(request):
    
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False
    
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and ProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            
            # Now sort out the Profile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the Profile model.
            #if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']
        
            # Now we save the Profile model instance.
            profile.save()
    
            # Update our variable to tell the template registration was successful.
            registered = True
        
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    # Render the template depending on the context.
    return render(request,
                  'bandit/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
        # because the request.POST.get('<variable>') returns None, if the value does not exist,
        # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/bandit/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Bandit account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'bandit/login.html', {})

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    
    # Take the user back to the homepage.
    return HttpResponseRedirect('/bandit/')


def band(request, band_profile_name_slug):
    context_dict = {}

    try:
        # Can we find a profile name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        profile = Profile.objects.get(slug=band_profile_name_slug)
        context_dict['profile'] = profile
        context_dict['profile_name'] = profile.name

        # Does this profile correspond to a band?
        # If not, the .get() method raises a DoesNotExist exception.
        band = Band.objects.get(profile=profile)
        context_dict['band'] = band

        # Is the user authenticated?
        if request.user.is_authenticated():
            profile = Profile.objects.get(user=request.user)

            # Is the user the owner of the profile?
            # If so, show 'Edit Profile' option
            if band.profile == profile:
                context_dict['accessed_by_owner'] = True

    except (Profile.DoesNotExist, Band.DoesNotExist):
        pass

    return render(request, 'bandit/band.html', context_dict)

def venue(request, venue_profile_name_slug):
    context_dict = {}

    try:
        # Can we find a profile name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        profile = Profile.objects.get(slug=venue_profile_name_slug)
        context_dict['profile'] = profile
        context_dict['profile_name'] = profile.name
        
        # Does this profile correspond to a venue?
        # If not, the .get() method raises a DoesNotExist exception.
        venue = Venue.objects.get(profile=profile)
        context_dict['venue'] = venue

        # Retrieve all the events of the specified venue.
        events = Event.objects.filter(venue=venue)
        context_dict['events'] = events

        # Is the user authenticated?
        if request.user.is_authenticated():
            profile = Profile.objects.get(user=request.user)

            # Is the user the owner of the profile?
            # If so, show 'Add Event' option
            if venue.profile == profile:
                context_dict['accessed_by_owner'] = True

    except (Profile.DoesNotExist, Venue.DoesNotExist):
        pass

    return render(request, 'bandit/venue.html', context_dict)

def event(request, venue_profile_name_slug, event_date_slug):
    context_dict = {}

    try:
        # Does this venue_profile_name_slug correspond to a venue?
        # If not, the .get() method raises a DoesNotExist exception.
        venue = Venue.objects.get(profile__slug=venue_profile_name_slug)
        context_dict['venue'] = venue

        # Can we find an event of that venue for that date?
        # If we can't, the .get() method raises a DoesNotExist exception.
        event = Event.objects.get(slug=event_date_slug, venue=venue)
        context_dict['event'] = event
        context_dict['event_name'] = event.name

        # Show user-specific content...
        if request.user.is_authenticated():
            profile = Profile.objects.get(user=request.user)
            context_dict['username'] = request.user.username

            # If the user is the venue-owner of the event, show the list of requests
            if venue.profile == profile:
                # Retrieve the requests for this event.
                requests = Request.objects.filter(event=event)
                context_dict['requests'] = requests

            # If the user is a band...
            # ... and hasn't requested to play this gig, show a 'Request' button.
            # ... and has requested to play this gig, show the date of request.
            try:
                band = Band.objects.get(profile=profile)
                context_dict['band'] = band
            except Band.DoesNotExist:
                band = None

            if not band == None:
                gig_request = Request.objects.get(event=event, band=band)
                context_dict['gig_request'] = gig_request

    except (Event.DoesNotExist, Profile.DoesNotExist, Venue.DoesNotExist, Request.DoesNotExist):
        pass

    return render(request, 'bandit/event.html', context_dict)

@login_required
def request(request, venue_profile_name_slug, event_date_slug, band_profile_name_slug):
    context_dict = {}

    try:
        # Does this venue_profile_name_slug correspond to a venue?
        # If not, the .get() method raises a DoesNotExist exception.
        venue = Venue.objects.get(profile__slug=venue_profile_name_slug)
        context_dict['venue'] = venue

        # Can we find an event of that venue for that date?
        # If we can't, the .get() method raises a DoesNotExist exception.
        event = Event.objects.get(slug=event_date_slug, venue=venue)

        # Is the user authenticated?
        # If not, contect_dict will remain empty.
        if request.user.is_authenticated():
            profile = Profile.objects.get(user=request.user)
            context_dict['username'] = request.user.username

            # Is the user the owner of the event?
            # If not, access to this information is denied!
            if event.venue.profile == profile:
                context_dict['event'] = event
                context_dict['event_name'] = event.name

                # Can we find a profile name slug with the given name?
                # If we can't, the .get() method raises a DoesNotExist exception.
                profile = Profile.objects.get(slug=band_profile_name_slug)

                # Does this profile correspond to a band?
                # If not, the .get() method raises a DoesNotExist exception.
                band = Band.objects.get(profile=profile)
                context_dict['band'] = band

                # Has this band made a request for this event?
                # If not, the .get() method raises a DoesNotExist exception.
                gig_request =  Request.objects.get(event=event, band=band)
                context_dict['gig_request'] = gig_request
                gig_request.seen = True
                gig_request.save()

                # Has the owner accepted a band for this event?
                # If not, an 'Accept' button should be shown...
                if event.band:
                    context_dict['accepted_band'] = event.band
            else:
                # The user is not the owner of the specified event.
                # We return a 403 (Forbidden)
                raise PermissionDenied

    except (Event.DoesNotExist, Band.DoesNotExist, Profile.DoesNotExist, Venue.DoesNotExist, Request.DoesNotExist):
        pass

    return render(request, 'bandit/request.html', context_dict)


def add_event(request, venue_profile_name_slug):
    context_dict = {}

    try:
        # Does this venue_profile_name_slug correspond to a venue?
        # If not, the .get() method raises a DoesNotExist exception.
        venue = Venue.objects.get(profile__slug=venue_profile_name_slug)

        # Is the user authenticated?
        # If not, contect_dict will remain empty.
        if request.user.is_authenticated():
            profile = Profile.objects.get(user=request.user)
            context_dict['venue_profile_name_slug'] = venue_profile_name_slug
            # Is the user the the owner of this venue?
            # If so, show him the form!
            if venue.profile == profile:
                # A HTTP POST?
                if request.method == 'POST':
                    form = EventForm(request.POST)

                    # Have we been provided with a valid form?
                    if form.is_valid():
                        # Save the new event to the database.
                        new_event = form.save(commit=False)
                        try:
                            existing_event = Event.objects.get(name=new_event.name, venue=venue, date=new_event.date)
                        except Exception, e:
                            new_event.venue = venue
                            new_event.save()
                        return event(request, venue.profile.slug, new_event.slug)
                    else:
                        # The supplied form contained errors - just print them to the terminal.
                        print form.errors
                else:
                    # If the request was not a POST, display the form to enter details.
                    form = EventForm()

                # Bad form (or form details), no form supplied...
                # Render the form with error messages (if any).
                context_dict['form'] = form
                return render(request, 'bandit/add_event.html', context_dict)

    except (Profile.DoesNotExist, Venue.DoesNotExist):
        pass

    # User is not authorised to add an event for the specified venue.
    # We return 403 (Forbidden)
    raise PermissionDenied

@login_required
def make_gig_request(request):
    event_id = None
    band_id = None
    if request.method == 'GET':
        event_id = request.GET['event_id']
        band_id = request.GET['band_id']

    new_gig_request = None
    response = ""
    if band_id and event_id:
        event = Event.objects.get(id=int(event_id))
        band = Band.objects.get(id=int(band_id))
        if band and event:
            # Continue only if band hasn't already made a request
            existing_gig_request = None
            try:
                existing_gig_request = Request.objects.get(event=event, band=band)
                response = "This request already exists!"
            except Exception, e:
                new_gig_request = Request.objects.get_or_create(event=event, band=band)[0]
                response = "Request sent."

    return HttpResponse(response)

@login_required
def edit_band_profile(request, band_profile_name_slug):
    context_dict = {}

    try:
        # Does this band_profile_name_slug correspond to a band?
        # If not, the .get() method raises a DoesNotExist exception.
        existing_band = Band.objects.get(profile__slug=band_profile_name_slug)
        context_dict['band_profile_name_slug'] = band_profile_name_slug

        # Is the user the owner of this profile?
        if existing_band.profile.user == request.user:
            # A HTTP POST?
            if request.method == 'POST':
                profile_form = EditProfileForm(request.POST, request.FILES, instance=existing_band.profile)
                band_form = BandForm(request.POST, instance=existing_band)

                # Have we been provided with valid forms?
                if profile_form.is_valid() and band_form.is_valid():
                    # Save the new category to the database.
                    profile_form.save(commit=True)
                    band_form.save(commit=True)

                    # Now call the index() view.
                    # The user will be shown the homepage.
                    return band(request, band_profile_name_slug)
                else:
                    # The supplied form contained errors - just print them to the terminal.
                    print profile_form.errors, band_form.errors
            else:
                # If the request was not a POST, display the form to enter details.
                profile_form = EditProfileForm(instance=existing_band.profile)
                band_form = BandForm(instance=existing_band)
                context_dict['profile_form'] = profile_form
                context_dict['band_form'] = band_form

            # Bad form (or form details), no form supplied...
            # Render the form with error messages (if any).
            return render(request, 'bandit/edit_band_profile.html', context_dict)
    except (Band.DoesNotExist):
        pass

    # User is not authorised to edit this profile.
    # We return 403 (Forbidden)
    raise PermissionDenied

@login_required
def edit_venue_profile(request, venue_profile_name_slug):
    context_dict = {}

    try:
        # Does this venue_profile_name_slug correspond to a venue?
        # If not, the .get() method raises a DoesNotExist exception.
        existing_venue = Venue.objects.get(profile__slug=venue_profile_name_slug)
        context_dict['venue_profile_name_slug'] = venue_profile_name_slug

        # Is the user the owner of this profile?
        if existing_venue.profile.user == request.user:
            # A HTTP POST?
            if request.method == 'POST':
                profile_form = EditProfileForm(request.POST, request.FILES, instance=existing_venue.profile)
                venue_form = VenueForm(request.POST, instance=existing_venue)

                # Have we been provided with valid forms?
                if profile_form.is_valid() and venue_form.is_valid():
                    # Save the new category to the database.
                    profile_form.save(commit=True)
                    venue_form.save(commit=True)

                    # Now call the index() view.
                    # The user will be shown the homepage.
                    return venue(request, venue_profile_name_slug)
                else:
                    # The supplied form contained errors - just print them to the terminal.
                    print profile_form.errors, venue_form.errors
            else:
                # If the request was not a POST, display the form to enter details.
                profile_form = EditProfileForm(instance=existing_venue.profile)
                venue_form = VenueForm(instance=existing_venue)
                context_dict['profile_form'] = profile_form
                context_dict['venue_form'] = venue_form

            # Bad form (or form details), no form supplied...
            # Render the form with error messages (if any).
            return render(request, 'bandit/edit_venue_profile.html', context_dict)
    except (Band.DoesNotExist):
        pass

    # User is not authorised to edit this profile.
    # We return 403 (Forbidden)
    raise PermissionDenied


@login_required
def accept_gig_request(request):
    event_id = None
    band_id = None
    if request.method == 'GET':
        event_id = request.GET['event_id']
        band_id = request.GET['band_id']

    response = ""
    if band_id and event_id:
        event = Event.objects.get(id=int(event_id))
        band = Band.objects.get(id=int(band_id))
        if band and event:
            # Is a band already booked for this event?
            # If so, return error message.
            # If not, book this band!
            if not event.band:
                event.band = band
                event.save()
                response = "Request accepted."
            else:
                response = "A band is already booked for this event."

    return HttpResponse(response)

# Should be called by all the other views!
def get_venue_notifications(request):
    try:
        # Is the user authenticated?
        if request.user.is_authenticated():
            # Is the user a venue?
            profile = Profile.objects.get(user=request.user)
            venue = Venue.objects.get(profile=profile)

            new_requests = Request.objects.filter(venue=venue, seen=False)

            return new_requests

    except (Profile.DoesNotExist, Venue.DoesNotExist):
        return None

def events(request):
    context_dict = {}
    today = date.today()
    event_list = Event.objects.filter(date__gte=today).order_by('date')
    context_dict['event_list'] = event_list
    return render(request, 'bandit/events.html', context_dict)

def bands(request):
    context_dict = {}
    band_list = Band.objects.order_by('-profile__name')
    context_dict['band_list'] = band_list
    return render(request, 'bandit/bands.html', context_dict)

def venues(request):
    context_dict = {}
    venue_list = Venue.objects.order_by('-profile__name')
    context_dict['venue_list'] = venue_list
    return render(request, 'bandit/venues.html', context_dict)