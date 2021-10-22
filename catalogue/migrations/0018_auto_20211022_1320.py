# Generated by Django 3.2.8 on 2021-10-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0017_auto_20211018_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='url',
            field=models.URLField(blank=True, help_text='Öffentlicher Link zur Lösung', verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='branchapplicable',
            name='name',
            field=models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('C10', 'Nahrungs- und Futtermittel'), ('C11', 'Getränke'), ('C12', 'Tabakverarbeitung'), ('C13', 'Textilien'), ('C14', 'Bekleidung'), ('C15', 'Leder, Lederwaren und Schuhe'), ('C16', 'Holz-, Flecht-, Korb- und Korkwaren (ohne Möbel)'), ('C17', 'Papier, Pappe und Waren daraus'), ('C18', 'Druckerzeugnisse; Vervielfältigung von bespielten Ton-, Bild und Datenträgern'), ('C19', 'Kokerei und Mineralölverarbeitung'), ('C20', 'Chemische Erzeugnisse'), ('C21', 'Pharmazeutischen Erzeugnisse'), ('C22', 'Gummi- und Kunststoffwaren'), ('C23', 'Glas und Glaswaren, Keramik, Verarbeitung von Steinen und Erden'), ('C24', 'Metallerzeugung und –bearbeitung'), ('C25', 'Metallerzeugnisse'), ('C26', 'Datenverarbeitungsgeräte, elektronische und optische Erzeugnisse'), ('C27', 'Elektrische Ausrüstungen'), ('C28', 'Maschinenbau'), ('C29', 'Kraftwagen und Kraftwagenteile'), ('C30', 'Sonstiger Fahrzeugbau'), ('C31', 'Möbel'), ('C32', 'Herstellung von sonstigen Waren'), ('ALL', 'Keine / Branchenunabhängig')], help_text='Branche, in der die Lösung anwendbar ist', max_length=3),
        ),
        migrations.AlterField(
            model_name='branchproven',
            name='name',
            field=models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('C10', 'Nahrungs- und Futtermittel'), ('C11', 'Getränke'), ('C12', 'Tabakverarbeitung'), ('C13', 'Textilien'), ('C14', 'Bekleidung'), ('C15', 'Leder, Lederwaren und Schuhe'), ('C16', 'Holz-, Flecht-, Korb- und Korkwaren (ohne Möbel)'), ('C17', 'Papier, Pappe und Waren daraus'), ('C18', 'Druckerzeugnisse; Vervielfältigung von bespielten Ton-, Bild und Datenträgern'), ('C19', 'Kokerei und Mineralölverarbeitung'), ('C20', 'Chemische Erzeugnisse'), ('C21', 'Pharmazeutischen Erzeugnisse'), ('C22', 'Gummi- und Kunststoffwaren'), ('C23', 'Glas und Glaswaren, Keramik, Verarbeitung von Steinen und Erden'), ('C24', 'Metallerzeugung und –bearbeitung'), ('C25', 'Metallerzeugnisse'), ('C26', 'Datenverarbeitungsgeräte, elektronische und optische Erzeugnisse'), ('C27', 'Elektrische Ausrüstungen'), ('C28', 'Maschinenbau'), ('C29', 'Kraftwagen und Kraftwagenteile'), ('C30', 'Sonstiger Fahrzeugbau'), ('C31', 'Möbel'), ('C32', 'Herstellung von sonstigen Waren'), ('ALL', 'Keine / Branchenunabhängig')], help_text='Branche, in der die Lösung bereits erfolgreich erprobt wurde; belegte Anwendung', max_length=3),
        ),
        migrations.AlterField(
            model_name='component',
            name='allow_email',
            field=models.BooleanField(default=True, help_text='Erlaubt die Einblendung eines Kontaktformulares.', verbose_name='Erlaube Kontaktaufnahme per Mail'),
        ),
        migrations.AlterField(
            model_name='component',
            name='published',
            field=models.BooleanField(default=False, help_text='Lösung bereit zur Veröffentlichung. Nach anschließender Moderation wird Ihre Lösung öffentlich zugänglich.', verbose_name='Veröffentlicht'),
        ),
        migrations.AlterField(
            model_name='component',
            name='trl',
            field=models.IntegerField(choices=[(None, 'Bitte Wert auswählen'), (1, 'TRL 1 - Grundprinzipien beobachtet'), (2, 'TRL 2 - Technologiekonzept formuliert'), (3, 'TRL 3 - Experimenteller Nachweis des Konzepts'), (4, 'TRL 4 - Technologie im Labor überprüft'), (5, 'TRL 5 - Technologie in relevanter Umgebung überprüft'), (6, 'TRL 6 - Technologie in relevanter Umgebung getestet'), (7, 'TRL 7 - Test eines System-Prototyps im realen Einsatz'), (8, 'TRL 8 - System ist komplett und qualifiziert'), (9, 'TRL 9 - System funktioniert in operationeller Umgebung')], help_text='Status der Lösung in Bezug auf Ihre Einsetzbarkeit durch die Angabe eines technischen Reifegrades (Technology Readiness Level).', verbose_name='TRL'),
        ),
        migrations.AlterField(
            model_name='corporatedivision',
            name='name',
            field=models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('CS', 'Kundendienst / Inbetriebnahme'), ('DD', 'Konstruktion / Entwicklung'), ('PA', 'Produktion / Montage'), ('MA', 'Instandhaltung'), ('LO', 'Logistik / Supply Chain Management'), ('MC', 'Marketing / Kommunikation'), ('MM', 'Materialwirtschaft / Einkauf'), ('AC', 'Rechnungswesen / Controlling'), ('CG', 'Management / Unternehmensführung'), ('SP', 'Sales / Preisgestaltung')], help_text='Bereich des produzierenden Unternehmens, für den die Lösung entwickelt wurde', max_length=2),
        ),
    ]
