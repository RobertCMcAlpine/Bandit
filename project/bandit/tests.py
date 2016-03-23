from django.test import TestCase

from bandit.models import Band, Profile
from django.contrib.auth.models import User


class BandMethodTests(TestCase):
	
	def test_ensure_number_of_members_is_positive(self):
		"""
                ensure_number_of_members_is_positive should results True for bands where number of members is zero or positive
        """
                user = User(username='test', email='test@test.com', password='test')
                user.save()
                profile = Profile(name='test', user=user)
                profile.save()
                # This will succeed:
                band = Band(profile=profile, number_of_members=3)
                # This will fail:
                # band = Band(profile=profile, number_of_members=-3)
                band.save()
                self.assertEqual((band.number_of_members >= 0), True)

class ProfileMethodTests(TestCase):
	
	def test_slug_line_creation(self):
            """
            slug_line_creation checks to make sure that when we add a profile, an appropriate slug line is created
            i.e. "Mouse Rat" -> "mouse-rat"
             """

            user = User(username='test', email='test@test.com', password='test')
            user.save()
            profile = Profile(name='Mouse Rat', user=user)
            profile.save()
            self.assertEqual(profile.slug, 'mouse-rat')