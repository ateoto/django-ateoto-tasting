from django.db import models
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager

class Roaster(models.Model):
    name = models.CharField(max_length = 100)
    website = models.URLField(blank = True)
    slug = models.SlugField(editable = False)
    
    def __unicode__(self):
        return u"%s" % (self.name)
                            
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        return super(Roaster, self).save(*args, **kwargs)

class Origin(models.Model):
    name = models.CharField(max_length = 100)
    notes = models.TextField(blank = True)
    slug = models.SlugField(editable = False)

    def __unicode__(self):
        return u"%s" % (self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(Origin, self).save(*args, **kwargs)

class Coffee(models.Model):
    PROCESSING_WET = 1
    PROCESSING_DRY = 2
    PROCESSING_SEMIDRY = 3

    PROCESSING_CHOICES = (
        (PROCESSING_WET, 'Wet'),
        (PROCESSING_DRY, 'Dry'),
        (PROCESSING_SEMIDRY, 'Semi Dry')
    )

    name = models.CharField(max_length = 100)
    roaster = models.ForeignKey(Roaster)
    origin = models.ManyToManyField(Origin, related_name='coffees')
    origin_notes = models.CharField(max_length = 100, blank = True)
    process = models.IntegerField(choices = PROCESSING_CHOICES)
    slug = models.SlugField(editable = False)

    def __unicode__(self):
        return u"%s" % (self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(Coffee, self).save(*args, **kwargs)

    @property
    def score(self):
        tastings = CoffeeTasting.objects.filter(coffee = self)
        number_of_tastings = tastings.count()
        if number_of_tastings > 0:
            aggregate_score = 0
            for tasting in tastings:
                aggregate_score += tasting.overall_score
            return aggregate_score / number_of_tastings
        else:
            return ''
    

class CoffeeTasting(models.Model):
    PREP_PRESS = 1
    PREP_VACPOT = 2
    PREP_CHEMEX = 3
    PREP_POUROVER = 4
    PREP_CUPPING = 5
    PREP_DRIP = 6

    PREP_CHOICES = (
        (PREP_PRESS, 'Press'),
        (PREP_VACPOT, 'Siphon'),
        (PREP_CHEMEX, 'Chemex'),
        (PREP_POUROVER, 'Pourover'),
        (PREP_CUPPING, 'Cupping'),
        (PREP_DRIP, 'Automatic Drip')
        )

    coffee = models.ForeignKey(Coffee)
    tasted_on = models.DateField()
    prep_method = models.IntegerField(choices = PREP_CHOICES)
    aroma_score = models.DecimalField(max_digits = 3, decimal_places = 1)
    taste_score = models.DecimalField(max_digits = 3, decimal_places = 1)
    body_score = models.DecimalField(max_digits = 3, decimal_places = 1)
    acidity_score = models.DecimalField(max_digits = 3, decimal_places = 1)
    aftertaste_score = models.DecimalField(max_digits = 3, decimal_places = 1)
    notes = models.TextField()
    overall_score = models.DecimalField(max_digits = 4, decimal_places = 1, editable = False)
    
    tags = TaggableManager()

    def __unicode__(self):
        return u"%s tasted on %s (%d)" % (self.coffee.name, self.tasted_on, self.overall_score)

    def save(self, *args, **kwargs):
        self.overall_score = (2 * (self.aroma_score + 
                                self.taste_score + 
                                self.body_score + 
                                self.acidity_score + 
                                self.aftertaste_score))
    
        return super(CoffeeTasting, self).save(*args, **kwargs)
