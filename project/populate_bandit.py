import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from bandit.models import Profile, Band, Venue, Event, Request, Image

from django.contrib.auth.models import User

from datetime import date, time

def populate():
	# Adding Leif's Band...
	leif_user = add_user("leifos", "leifos@itech.com", "leifos")
	leif_profile = add_profile(leif_user, "Leif's band", "-", "Glasgow",
		"02392561857", "The coolest band ever.", "B", "www.leifos.com")
	leif_band = add_band(leif_profile, 3, "Rock")

	# Adding Crappy Maths LT Venue...
	maths_user = add_user("david", "david@itech.com", "david")
	maths_profile = add_profile(maths_user, "Crappy Maths Lecture Theatre",  "-", "Glasgow",
		"02392561857", "Built in 1950", "V", "www.mathsbld.com")
	maths_venue = add_venue(maths_profile, "University Of Glasgow", "G12 8AB")

	# Adding Laura's pub
	laura_user = add_user("laura", "laura@itech.com", "david")
	laura_profile = add_profile(laura_user, "Laura's Pub",  "-", "Glasgow",
		"02392561857", "Best pub in town.", "V", "www.lauraspub.co.uk")
	laura_venue = add_venue(laura_profile, "7 Pub str", "G12 8AB")

	# Adding an event for Crappy Maths LT
	maths_event = add_event(maths_venue, leif_band, "ITECH Presentation", date(2016,3,23),
		time(14,00,00), time(17,00,00), "An A1 in ITECH!", "The event of the year!")

	# Adding an event for Laura's Pub
	laura_event = add_event(laura_venue, "-", "Friday Night Live", date(2016,3,25),
		time(19,30,00), time(22,00,00), "Free beer", "Beer and live music.")

	# Adding a request from Leif's band to play in the Maths event
	add_request(maths_event, leif_band)

	# Adding a request from Leif's band to play in Laura's event
	add_request(laura_event, leif_band)

	# Adding a few pictures...
	add_image(leif_profile, "media/images/leifos_prof.png", "profile pic")
	add_image(laura_profile, "media/images/pub01.jpg", "pub pic")
	add_image(laura_profile, "media/images/pub02.jpg", "pub pic")
	add_image(laura_profile, "media/images/pub_prof.jpg", "prof pic")
	add_image(maths_profile, "media/images/maths_prof.jpg", "prof pic")


def add_user(username, email, password):
	u = User.objects.get_or_create(username=username)[0]
	u.email = email
	u.password = password
	u.save()
	return u

def add_profile(user, name, profile_picture, city, phone, desc, profile_type, website):
	p = Profile.objects.get_or_create(user=user)[0]
	p.name = name
	if not profile_picture == "-":
		p.profile_picture = profile_picture
	p.city = city
	p.phone_number = phone
	p.description = desc
	p.profile_type = profile_type
	p.website = website
	p.save()
	return p

def add_band(profile, number_of_members, genre):
	b = Band.objects.get_or_create(profile=profile, number_of_members=number_of_members)[0]
	b.genre = genre
	b.save()
	return b

def add_venue(profile, address,post_code):
	v = Venue.objects.get_or_create(profile=profile)[0]
	v.address = address
	v.post_code = post_code
	v.save()
	return v

def add_event(venue, band, name, date, start_time, end_time, reward, description):
	e = Event.objects.get_or_create(venue=venue, date=date, start_time=start_time)[0]
	if not band == "-":
		e.band = band
	e.name = name
	e.end_time = end_time
	e.reward = reward
	e.description = description
	e.save()
	return e

def add_request(event, band):
	r = Request.objects.get_or_create(event=event, band=band)[0]
	return r

def add_image(profile, path, alt):
	i=Image.objects.get_or_create(profile=profile,path=path)[0]
	i.alt = alt
	i.save()
	return i

if __name__ == '__main__':
	print "Starting Bandit population script..."
	populate()
	print "... Done!"