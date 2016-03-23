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

	# Adding Andy's band, Mouse Rat...
	andy_user = add_user("andy", "andy@itech.com", "andy")
	andy_profile = add_profile(andy_user, "Mouse Rat", "-", "Pawnee",
		"02392561857", "You think you found love, but you're standing in The Pit...", "B", "www.mouse-rat.com")
	andy_band = add_band(andy_profile, 3, "Rock")

	#Adding Myron's band, Weird Sisters
	myron_user = add_user("myron", "myron@wizard.com", "myron")
	myron_profile = add_profile(myron_user, "Weird Sisters", "-", "London",
		"05647234080", "Eccentric glam-rockers with wands", "B", "www.weird-sisters.com")
	myron_band = add_band(myron_profile, 6, "Unclassifiable")

	#Adding Ulysses' band, The Soggy Bottom Boys
	ulysses_user = add_user("ulysses", "obrother@where.com", "ulysses")
	ulysses_profile = add_profile(ulysses_user, "The Soggy Bottom Boys", "-", "Mississippi",
		"01982477585", "Treasure, what treasure? We just want to sing!", "B", "www.soggy-bottom-boys.com")
	ulysses_band = add_band(ulysses_profile, 3, "Folk")

	#Adding Jake's band, The Blues Brothers
	jake_user = add_user("jake", "bbros@mail.com", "jake")
	jake_profile = add_profile(jake_user, "The Blues Brothers", "-", "Illinois",
		"01982477585", "We may be a duo just now but we'll be back to a band of 10 soon!", "B", "www.blues-bros.com")
	jake_band = add_band(jake_profile, 2, "Blues/R&B")

	#Adding Nigel's band, Spinal Tap
	nigel_user = add_user("nigel", "spinaltap@mail.com", "nigel")
	nigel_profile = add_profile(nigel_user, "Spinal Tap", "-", "Edinburgh",
		"0105769445", "We will turn it up to 11 and rock your event!", "B", "www.spinal-tap.com")
	nigel_band = add_band(nigel_profile, 2, "Rock")


	# Adding Crappy Maths LT Venue...
	maths_user = add_user("david", "david@itech.com", "david")
	maths_profile = add_profile(maths_user, "Crappy Maths Lecture Theatre",  "-", "Glasgow",
		"02392561857", "Built in 1950", "V", "www.mathsbld.com")
	maths_venue = add_venue(maths_profile, "University Of Glasgow", "G12 8AB")

	# Adding Laura's pub
	laura_user = add_user("laura", "laura@itech.com", "laura")
	laura_profile = add_profile(laura_user, "Laura's Pub",  "-", "Glasgow",
		"02392561857", "Best pub in town.", "V", "www.lauraspub.co.uk")
	laura_venue = add_venue(laura_profile, "7 Pub str", "G12 8AB")

	# Adding GUU Venue...
	guu_user = add_user("fergus", "fergus@guu.com", "fergus")
	guu_profile = add_profile(guu_user, "Glasgow University Union",  "-", "Glasgow",
		"02039096532", "Run by students for students", "V", "www.guu.co.uk")
	guu_venue = add_venue(guu_profile, "University Of Glasgow", "G12 8AB")

	# Adding Electric Circus Venue...
	ec_user = add_user("jerry", "jerry@ecircus.com", "jerry")
	ec_profile = add_profile(ec_user, "Electric Circus",  "-", "Edinburgh",
		"02039573343", "A rough exterior belies a slick and comfortably compact interior, with a capacity of 250", "V", "www.guu.co.uk")
	ec_venue = add_venue(ec_profile, "35 Market Street", "EH1")

	# Adding Barfly Venue...
	barfly_user = add_user("lucy", "lucy@barfly.com", "lucy")
	barfly_profile = add_profile(barfly_user, "Barfly",  "-", "London",
		"078852218453", "The Barfly champions cool and upcoming talent, making it a destination for music fans and partygoers alike" "V", "www.barfly.co.uk")
	barfly_venue = add_venue(barfly_profile, "49 Chalk Farm Road", "NW1 8AN")

	# Adding an event for Crappy Maths LT
	maths_event = add_event(maths_venue, leif_band, "ITECH Presentation", date(2016,3,23),
		time(14,00,00), time(17,00,00), "An A1 in ITECH!", "The event of the year!")

	# Adding an event for Laura's Pub
	laura_event = add_event(laura_venue, "-", "Friday Night Live", date(2016,3,25),
		time(19,30,00), time(22,00,00), "Free beer", "Beer and live music.")

	# Adding an event for GUU
	guu1_event = add_event(guu_venue, "-", "Daft Friday", date(2016,12,16),
		time(20,00,00), time(08,00,00), "Membership for Life", "12 hours of fun in finest black-tie.")

	# Adding an event for GUU
	guu2_event = add_event(guu_venue, "-", "Sessions @ The Well", date(2016,3,31),
		time(21,30,00), time(23,30,00), "Free beer", "Variety of Live Performances, best enjoyed with a pint of fun!")

	# Adding an event for Electric Circus
	ec1_event = add_event(ec_venue, "-", "Electric Sessions - Finger Pickin Good", date(2016,4,1),
		time(20,30,00), time(22,30,00), "Free Beer", "Live Music")

	# Adding an event for Electric Circus
	ec2_event = add_event(ec_venue, "-", "Electric Sessions - Finger Pickin Good", date(2016,4,7),
		time(20,30,00), time(22,30,00), "Free Beer", "Live Music")

	# Adding an event for Barfly
	barfly_event = add_event(ec_venue, "-", "Rock the Mic", date(2016,6,28),
		time(19,30,00), time(23,30,00), "Free Beer and publicity", "Flock to the stage as our latest acts take the mic")

	# Adding a request from Leif's band to play in the Maths event
	add_request(maths_event, leif_band)

	# Adding a request from Leif's band to play in Laura's event
	add_request(laura_event, leif_band)

	#Adding a request for Spinal Tap to play Electric Circus' event
	add_request(ec1_event, nigel_band)

	#Adding a request for Spinal Tap to play Electric Circus' event
	add_request(ec2_event, myron_band)

	#Adding a request for The Soggy Bottom Boys to play GUU's event
	add_request(guu1_event, ulysses_band)

	#Adding a request for The Blues Brothers to play GUU's event
	add_request(guu1_event, jake_band)

	#Adding a request for Leif's Band to play GUU's event
	add_request(guu1_event, leif_band)

	#Adding a request for Weird Sisters to play Barfly's event
	add_request(barfly_event, nigel_band)

	#Adding a request for Mouse Rat to play GUU's event
	add_request(guu2_event, andy_band)

	# Adding a few pictures...
	add_image(leif_profile, "media/images/leifos_prof.png", "profile pic")
	add_image(laura_profile, "media/images/pub01.jpg", "pub pic")
	add_image(laura_profile, "media/images/pub02.jpg", "pub pic")
	add_image(laura_profile, "media/images/pub_prof.jpg", "prof pic")
	add_image(maths_profile, "media/images/maths_prof.jpg", "profile pic")
	add_image(myron_profile, "media/images/ws_prof.jpg", "profile pic")
	add_image(jake_profile, "media/images/bb_prof.jpg", "profile pic")
	add_image(nigel_profile, "media/images/spinal_prof.jpg", "profile pic")
	add_image(guu_profile, "media/images/guu_prof.jpg", "profile pic")
	add_image(barfly_profile, "media/images/barfly_prof.jpg", "profile pic")

def add_user(username, email, password):
	u = User.objects.get_or_create(username=username)[0]
	u.email = email
	u.password = password
	u.set_password(u.password)
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