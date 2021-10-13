from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL


MANSIONI_TIPI = (
    ('VE', 'Verificatore'),
    ('VI', 'Vigilantes'),
    ('VO', 'Volontario'),
)

EVENTI_TIPI = (
    ('IM',      'In servizio di mattina'),
    ('IS',      'In servizio di sera'),
    ('I2S',     'In servizio di seconda serata'),
    ('ASS',     'Assente'),
    ('VIME',    'Visita medica'),
    ('A33',     'Articolo 33'),
    ('LIC',     'In licenza'),
    ('MAL',     'In malattia'),
    ('ALTRO',   'Altro'),
)

POLO_OPZ = (
    ('R1',      'Rimessa 1'),
    ('R8',      'Rimessa 8'),
    ('AL',      'P.za Borsellino'),
    ('ST',      'Stazione Centrale'),
    ('RP',      'P.za Repubblica'),
    ('PB',      'P.za Borsa'),
    ('SZ',      'P.za Sanzio'),
    ('OB',      'Due Obelischi'),
    ('NE',      'Nesima'),
    ('FN',      'Fontanarossa'),
    ('VA',      'Villaggio S\'Agata'),
)

FASCIA_OPZ = (
    ('M',        'Mattinale'), 
    ('S',        'Serale'), 
    ('S2',       'Seconda Serata'),
)

GIORNO_RIPOSO = (
    (7,        '1° Domenica'),
    (14,       '2° Domenica'),
    (21,       '3° Domenica'),
    (28,       '4° Domenica'),
    (35,       '5° Domenica'),
    (42,       '6° Domenica'),
    (49,       '7° Domenica'),
    (56,       '8° Domenica'),
    (63,       '9° Domenica'),
    (70,       '10° Domenica'),
    (77,       '11° Domenica'),
    (83,       'Sabato'),
    (89,       'Venerdi'),
    (95,       'Giovedi'),
    (101,      'Mercoledi'),
    (107,      'Martedi'),
    (1,        'Lunedi'),
)

class SequenzaRiposi(models.Model):
    nome                        = models.CharField(max_length=50, unique=True)
    sequenza                    = models.TextField()

    class Meta:
        verbose_name_plural     = "Sequenze Riposi"
        ordering                = ["nome"]

    def __str__(self):
        return self.nome

#TODO: Rinomina campi: data_inizio... e indice_in...
class Lavoratore(models.Model):
    matricola           = models.CharField(max_length=5, unique=True, blank=True)
    nominativo          = models.CharField(max_length=50)
    mansione            = models.CharField(max_length=2, choices=MANSIONI_TIPI)
    sequenza_riposi     = models.ForeignKey(SequenzaRiposi, on_delete=models.SET_NULL, null=True, blank=True)
    #data_di_riferimento_per_sequenza_riposi 
    data_per_sequenza   = models.DateField("data di riferimento ...", null=True, blank=True)
    #indice_giorno_di_riferimento_per_sequenza_riposi   
    indice_per_sequenza = models.IntegerField("corrisponde alla ...", null=True, blank=True, choices=GIORNO_RIPOSO)

    class Meta:        
        verbose_name_plural     = "Lavoratori"
        ordering                = ["nominativo"]
    
    def __str__(self):
        return self.nominativo


class Linea(models.Model):
    nome                        = models.CharField(primary_key=True, unique=True, max_length=5)      
    polo                        = models.CharField(max_length=2, blank=True, null=True, default='R8', choices=POLO_OPZ,)
    descrizione                 = models.CharField(max_length=255, blank=True, null=True)      

    class Meta:
        verbose_name_plural     = "Linee"
        ordering                = ['nome']

    def __str__(self):
        return self.nome


class Turno(models.Model):
    empty_value_display         = '---'
    mansione                    = models.CharField(max_length=2, choices=MANSIONI_TIPI)
    priorita                    = models.IntegerField(default=99)
    linea                       = models.ForeignKey(Linea, to_field='nome', on_delete=models.SET_NULL, blank=True, null=True)
    fascia                      = models.CharField(max_length=2, blank=True, null=True, choices=FASCIA_OPZ,)
    ora_inizio                  = models.TimeField()
    ora_fine                    = models.TimeField()    
    polo_monta                  = models.CharField(max_length=2, blank=True, null=True, choices=POLO_OPZ,)
    note                        = models.TextField(max_length=100, blank=True)
    
    class Meta:
        verbose_name_plural     = "Turni"
        ordering                = ['ora_inizio', 'polo_monta']
        #constraints             = [models.UniqueConstraint(fields=['mansione', 'linea', 'ora_inizio', 'ora_fine', 'polo_monta'], name='unique_turno')]

    def __str__(self):
        return ('%s %s %s %s %s %s %s' % (self.mansione, self.priorita, self.linea, self.ora_inizio.strftime("%H:%M"), self.ora_fine.strftime("%H:%M"), self.polo_monta, self.note))


class Matrice(models.Model):
    data                        = models.DateField(auto_now_add=True)
    nome                        = models.CharField(unique=True, max_length=20)
    turni                       = models.ManyToManyField(Turno)
    
    class Meta:
        verbose_name_plural     = "Matrici"
        ordering                = ['nome']

    def __str__(self):
        return ('%s del %s' % (self.nome, self.data.strftime("%d %B %Y")))

class Evento(models.Model):
    data                        = models.DateField()
    lavoratore                  = models.ForeignKey(Lavoratore, on_delete=models.CASCADE)
    tipologia                   = models.CharField(max_length=5, choices=EVENTI_TIPI)
    turno                       = models.ForeignKey(Turno, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural     = "Eventi"
        ordering                = ['data', 'lavoratore']