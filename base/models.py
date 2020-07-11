from django.db import models

# Create your models here.
class APForm(models.Model):
    coursenames=models.CharField(max_length=250)
    class Meta:
        db_table = "newcourses"
    '''
    choices=[('none','none'),('*Art History - 5 waive ARTH101','*Art History - 5 waive ARTH101'),('*Art History - 5 waive ARTH102','*Art History - 5 waive ARTH102'),('Chemistry - 5','Chemistry - 5'),('Computer Science A - 5','Computer Science A - 5'),('Computer Science AB - 5','Computer Science AB - 5'),('Computer Science AB - 4','Computer Science AB - 4'),('Economics Micro - 5','Economics Micro - 5'),('Economics Macro - 5','Economics Macro - 5'),('French Language - 5','French Language - 5'),('French Literature - 5','French Literature - 5'),('German Language - 5','German Language - 5'),('Italian Language and Culture - 5','Italian Language and Culture - 5'),('Latin - 5','Latin - 5'),('Latin - Literature - 5','Latin - Literature - 5'),('Latin - Vergil - 5','Latin - Vergil - 5'),('Mathematics BC - 5','Mathematics BC - 5'),('Physics-B - 5','Physics-B - 5'),('Physics 1 - 5','Physics 1 - 5'),('Physics 2 - 5','Physics 2 - 5'),('Physics-C Mechanics - 5','Physics-C Mechanics - 5'),('Physics-C Electricity and Magnetism - 5','Physics-C Electricity and Magnetism - 5'),('Psychology - 5','Psychology - 5'),('Spanish Language - 5','Spanish Language - 5'),('Spanish Literature - 5','Spanish Literature - 5'),('*Statistics - 5 waive STAT101','*Statistics - 5 waive STAT101'),('*Statistics - 5 waive STAT111','*Statistics - 5 waive STAT111')]

    AP = forms.MultipleChoiceField(
    required=False,
    widget=forms.CheckboxSelectMultiple,
    choices= choices
    )
    '''