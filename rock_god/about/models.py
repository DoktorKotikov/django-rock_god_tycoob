from django.db import models
from django.urls import reverse
# Create your models here.

class Index(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    image_path = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    city_name = models.CharField(max_length=100, help_text='Enter name of city')
    population = models.IntegerField(help_text='Enter population of the city')
    fans_need = models.IntegerField(help_text='Enter number of fans to open city')
    gig = models.ForeignKey('Gig', null=True, on_delete=models.SET_NULL, blank=True)
    studio = models.ForeignKey('RecordDeal', null=True, on_delete=models.SET_NULL, blank=True)
    record = models.ForeignKey('RecordingStudio', null=True, on_delete=models.SET_NULL, blank=True)
    video = models.ForeignKey('VideoClip', null=True, on_delete=models.SET_NULL, blank=True)
    hospital = models.ForeignKey('Hospital', null=True, on_delete=models.SET_NULL, blank=True)
    pub = models.ForeignKey('Pub', null=True, on_delete=models.SET_NULL, blank=True)
    strip = models.ForeignKey('Strip', null=True, on_delete=models.SET_NULL, blank=True)
    fastfood = models.ForeignKey('Fastfood', null=True, on_delete=models.SET_NULL, blank=True)
    map = models.CharField(max_length=1000, null=True, blank=True)
    x = models.IntegerField(null=True, blank=True)
    y = models.IntegerField(null=True, blank=True)
    pub_x = models.IntegerField(null=True, blank=True)
    pub_y = models.IntegerField(null=True, blank=True)
    strip_x = models.IntegerField(null=True, blank=True)
    strip_y = models.IntegerField(null=True, blank=True)
    hospital_x = models.IntegerField(null=True, blank=True)
    hospital_y = models.IntegerField(null=True, blank=True)
    fastfood_x = models.IntegerField(null=True, blank=True)
    fastfood_y = models.IntegerField(null=True, blank=True)


    class Meta:
        ordering = ['fans_need']

    def __str__(self):
        return f'{self.city_name}'


    def get_absolute_url(self):
        return reverse('city-detail', args=[str(self.id)])



class Gig(models.Model):
    club_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    ticket_value = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField(null=True, blank=True)
    min_bandrating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    grade = models.CharField(max_length=3, null=True, blank=True)
    x = models.IntegerField(null=True, blank=True)
    y = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.club_name}'

    def get_absolute_url(self):
        return reverse('gig-detail', args=[str(self.id)])

class RecordDeal(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    record_rank = models.CharField(max_length=3, null=True, blank=True)
    min_bandrating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    min_fans = models.IntegerField(null=True, blank=True)
    min_albums = models.IntegerField(null=True, blank=True)
    min_albumrating = models.IntegerField(null=True, blank=True)
    distribution_power = models.IntegerField(null=True, blank=True)
    revenue_share = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    album_type = models.CharField(max_length=100, null=True, blank=True)
    studio_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    studio_locations = models.ForeignKey('RecordingStudio', null=True, on_delete=models.SET_NULL, blank=True)
    videoclip_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    videoclip_count = models.IntegerField(null=True, blank=True)
    videoclip_locations = models.ForeignKey('VideoClip', null=True, on_delete=models.SET_NULL, blank=True)
    upfront_money = models.IntegerField(null=True, blank=True)
    revenue_affect = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    songs_required = models.IntegerField(null=True, blank=True)
    songs_minimum_rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    videoclips_required = models.IntegerField(null=True, blank=True)
    gigs_required = models.IntegerField(null=True, blank=True)
    gigs_locations = models.ManyToManyField(Gig)
    fine_amount = models.IntegerField(null=True, blank=True)
    cancel_cooldown = models.IntegerField(null=True, blank=True)
    due_date = models.IntegerField(null=True, blank=True)
    x = models.IntegerField(null=True, blank=True)
    y = models.IntegerField(null=True, blank=True)



    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('recorddeals-detail', args=[str(self.id)])


class RecordingStudio(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    song_cost_record = models.IntegerField(null=True, blank=True)
    song_cost_rehearsal = models.IntegerField(null=True, blank=True)
    studio_quality = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    min_bandrating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    grade = models.CharField(max_length=3, null=True, blank=True)
    x = models.IntegerField(null=True, blank=True)
    y = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('recordstudios-detail', args=[str(self.id)])

class VideoClip(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    studio_quality = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    grade = models.CharField(max_length=3, null=True, blank=True)
    x = models.IntegerField(null=True, blank=True)
    y = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('videoclip-detail', args=[str(self.id)])


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    cost_one_person = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('hospital-detail', args=[str(self.id)])



class Pub(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    cost_one_person = models.IntegerField(null=True, blank=True)
    tension_decrease_one_hour = models.IntegerField(null=True, blank=True)
    tension_decrease_two_hour = models.IntegerField(null=True, blank=True)
    tension_decrease_three_hour = models.IntegerField(null=True, blank=True)
    tension_decrease_four_hour = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('pub-detail', args=[str(self.id)])


class Strip(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    cost_one_person = models.IntegerField(null=True, blank=True)
    tension_decrease_one_hour = models.IntegerField(null=True, blank=True)
    tension_decrease_two_hour = models.IntegerField(null=True, blank=True)
    tension_decrease_three_hour = models.IntegerField(null=True, blank=True)
    tension_decrease_four_hour = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('strip-detail', args=[str(self.id)])


class Fastfood(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    cost_one_person = models.IntegerField(null=True, blank=True)
    tension_decrease_one_hour = models.IntegerField(null=True, blank=True)
    tension_decrease_two_hour = models.IntegerField(null=True, blank=True)
    tension_decrease_three_hour = models.IntegerField(null=True, blank=True)
    tension_decrease_four_hour = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


    def get_absolute_url(self):
        return reverse('fastfood-detail', args=[str(self.id)])
