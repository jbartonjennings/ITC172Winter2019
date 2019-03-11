from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.
class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='Best Meeting Ever')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

class MeetingMinutesTest(TestCase):
    def test_stringOutput(self):
        meetingminutes=MeetingMinutes(minutes='Sixty')
        self.assertEqual(str(meetingminutes), meetingminutes.minutes)

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'MeetingMinutes')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='Awesome Resource')
        self.assertEqual(str(resource), resource.resourcename)

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'Resource')

class EventTest(TestCase):
    def test_stringOutput(self):
        event=Event(eventtitle='Kickass Event')
        self.assertEqual(str(event), event.eventtitle)

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'Event')

class New_Product_Form_Test(TestCase):

    
    def test_meetingForm_is_valid(self):
        form = MeetingForm(data={'meetingtitle': "Sweetest meeting on earth", 'meetingdate': "June 20 1979", 'meetingtime': "sweetest time ever", 'meetinglocation': "arguably the coolest place on earth", 'meetingagenda': "coming up with the coolest shit ever"})  })
        self.assertTrue(form.is_valid())

    def test_meetingForm_is_invalid(self):
        form = MeetingForm(data={'meetingtitle': "Sweetest meeting on earth", 'meetingdate': "June 21 1979", 'meetingtime': "sweetest time ever", 'meetinglocation': "arguably the coolest place on earth", 'meetingagenda': "coming up with the coolest shit ever"})  })
        self.assertFalse(form.is_valid())

