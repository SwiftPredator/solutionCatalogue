# Generated by Django 3.1.4 on 2021-01-18 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField(help_text='Hergestelltes Produkt', verbose_name='Produkt')),
            ],
            options={
                'verbose_name': 'Anwendungsprofil',
                'verbose_name_plural': 'Anwendungsprofil',
            },
        ),
        migrations.CreateModel(
            name='BaseData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Bezeichnung der Komponente', max_length=200, unique=True, verbose_name='Name')),
                ('trl', models.IntegerField(choices=[(None, 'Bitte Wert auswählen'), (1, 'TRL 1 - Grundprinzipien beobachtet'), (2, 'TRL 2 - Technologiekonzept formuliert'), (3, 'TRL 3 - Experimenteller Nachweis des Konzepts'), (4, 'TRL 4 - Technologie im Labor überprüft'), (5, 'TRL 5 - Technologie in relevanter Umgebung überprüft'), (6, 'TRL 6 - Technologie in relevanter Umgebung getestet'), (7, 'TRL 7 - Test eines System-Prototyps im realen Einsatz'), (8, 'TRL 8 - System ist komplett und qualifiziert'), (9, 'TRL 9 - System funktioniert in operationeller Umgebung')], help_text='Status der Komponente in Bezug auf Ihre Einsetzbarkeit durch die Angabe eines Technischen Reifegrades (Technology Readiness Level).', verbose_name='TRL')),
                ('description', models.TextField(help_text='Kurze Beschreibung der Komponente', verbose_name='Kurzbeschreibung')),
            ],
            options={
                'verbose_name': 'Grunddaten',
                'verbose_name_plural': 'Grunddaten',
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Erstellt')),
                ('lastmodified_at', models.DateTimeField(auto_now=True, verbose_name='Zuletzt bearbeitet')),
                ('published', models.BooleanField(default=False, verbose_name='Veröffentlicht')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'KI Lösung',
                'verbose_name_plural': 'KI Lösungen',
            },
        ),
        migrations.CreateModel(
            name='Use',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scenarios', models.TextField(help_text='Beschreibung von Szenarien, in denen die Komponente bereits erfolgreich eingesetzt wurde', verbose_name='Szenarien / Use cases')),
                ('component', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalogue.component')),
            ],
            options={
                'verbose_name': 'Nutzen',
                'verbose_name_plural': 'Nutzen',
            },
        ),
        migrations.CreateModel(
            name='TechnicalSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realtime_processing', models.IntegerField(choices=[(None, 'Bitte Wert auswählen'), (0, 'Keine Echtzeit'), (1, 'Weiche Echtzeit'), (2, 'Harte Echtzeit'), (3, 'Feste Echtzeit')], help_text='Klassifizierung der Komponente in Bezug auf ihre Echtzeitfähigkeit', verbose_name='Echtzeitverarbeitung')),
                ('data_formats', models.CharField(blank=True, help_text='Datenformate, die von der KI-Komponente verarbeitet werden können und Datenformat der Ergebnisse', max_length=1000, verbose_name='Datenformate')),
                ('component', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalogue.component')),
            ],
            options={
                'verbose_name': 'Technische Spezifikation',
                'verbose_name_plural': 'Technische Spezifikation',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('PMCM', 'Predictive Maintenance/Condition Monitoring'), ('QCM', 'Qualitätskontrolle und –management'), ('OPP', 'Optimierte Prozessplanung'), ('OPC', 'Optimierte Prozesssteuerung'), ('RAS', 'Robotik & autonome Systeme'), ('IST', 'Intelligente Sensorik'), ('KM', 'Wissensmanagement'), ('FPA', 'Vorhersagen und Predictive Analytics'), ('ORS', 'Optimiertes Ressourcenmanagement'), ('IA', 'Intelligente Automatisierung'), ('IAS', 'Intelligente Assistenzsysteme'), ('DA', 'Datenanalyse'), ('DM', 'Data Management'), ('VAR', 'Virtuelle und erweiterte Realität'), ('OTHER', 'Sonstiges?')], help_text='Art der Aufgabe, der die beschriebene KI-Komponente zugeordnet werden kann (z.B. Predictive Maintenance, Qualitätsprüfung))', max_length=5)),
                ('base_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.basedata')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(help_text='Entwickler und/oder Hersteller der Komponente', max_length=1000, verbose_name='Hersteller')),
                ('contact', models.TextField(blank=True, help_text='Möglichkeit zum Hersteller Kontakt aufzunehmen', verbose_name='Kontakt')),
                ('additional_info', models.TextField(blank=True, help_text='Zusatzinformation zur Komponente', verbose_name='Zusatzinformationen')),
                ('component', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalogue.component')),
            ],
            options={
                'verbose_name': 'Quelle',
                'verbose_name_plural': 'Quelle',
            },
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocols', models.CharField(help_text='Schnittstellen und/oder Protokolle, die von der Kompomente unterstützt werden', max_length=1000, verbose_name='Protokolle/Schnittstellen')),
                ('it_environment', models.CharField(help_text='Anforderungen an die IT-Umgebung (inkl. IT Hardware) und an weitere Software/Bibliotheken, die für den Betrieb der Komponente notwendig sind', max_length=1000, verbose_name='IT Umgebung/Software')),
                ('hardware_requirements', models.CharField(help_text='Spezielle Hardware, welche für den Betrieb der Komponente notwendig ist (z.B. Kamera, Roboter)', max_length=1000, verbose_name='Spezielle Hardware')),
                ('devices', models.CharField(help_text='Maschinen und IoT Devices, mit denen die Komponente kompatibel ist', max_length=1000, verbose_name='Maschinen/Steuerungen')),
                ('component', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalogue.component')),
            ],
            options={
                'verbose_name': 'Vorraussetzungen',
                'verbose_name_plural': 'Vorraussetzungen',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=100, verbose_name='Unternehmen')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('PD', 'Produktionsentwicklung'), ('PA', 'Fertigungs- und Montagevorbereitung'), ('PP', 'Produktionsplanung und –steuerung'), ('PM', 'Teilefertigung'), ('PMPP', 'Teilefertigung - Produktionsprozess (Prozesskette)'), ('PMSP', 'Teilefertigung - Einzelfertigungsprozess'), ('AS', 'Montage, (VDI 2860)'), ('QA', 'Qualitätssicherung'), ('MFL', 'Materialfluss, Logistik'), ('CP', 'Änderungsprozesse'), ('PRODM', 'Produktionsinstandhaltung')], help_text='Prozess der durch die KI-Komponente unterstützt wird', max_length=5)),
                ('application_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.applicationprofile')),
            ],
            options={
                'verbose_name': 'Prozess',
                'verbose_name_plural': 'Prozess',
            },
        ),
        migrations.CreateModel(
            name='Licenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('FW', 'Freeware'), ('OSCL', 'Open Source / copy left'), ('OS', 'Open Source / no copy left'), ('PRO', 'Proprietär')], help_text='Welche Lizenzen bringt die Komponente mit, insbesondere Open Source Lizenzen', max_length=4, verbose_name='Typ')),
                ('name', models.CharField(blank=True, help_text='Genaue Angabe der Lizenz', max_length=1000)),
                ('technical_specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.technicalspecification')),
            ],
            options={
                'verbose_name': 'Lizenz',
                'verbose_name_plural': 'Lizenzen',
            },
        ),
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('E1', 'Effizienz - Bearbeitungszeit pro Anfrage (h)'), ('E2', 'Effizienz - Termintreue (%)'), ('E3', 'Effizienz - Rüstzeitanteil (%)'), ('E4', 'Effizienz - Automatisierungsgrad (%)'), ('E5', 'Effizienz - Durchlaufzeit (Tage)'), ('E6', 'Effizienz - Durchsatz (VDMA)'), ('E7', 'Effizienz - Produktionsvolumen/Zählwert'), ('E8', 'Effizienz - Stillstandzeit/Anzahl und Dauer ungeplanter Produktionsausfälle'), ('E9', 'Effizienz - Taktrate'), ('E10', 'Effizienz - Taktzeit'), ('Q1', 'Qualität - Qualitätsmängel'), ('Q2', 'Qualität - Rückgabequote'), ('Q3', 'Qualität - Right first Time/ Nacharbeitsquote / First Pass Yield (FPY, VDMA)'), ('Q4', 'Qualität - Fall-off-rate (VDMA)'), ('Q5', 'Qualität - Reklamationsquote (%)'), ('Q6', 'Qualität - Ausschussquote (%) / Ausschussgrad (VDMA)'), ('Q7', 'Qualität - Qualitätsgrad (%)'), ('Q8', 'Qualität - Fehlproduktionsquote (%)'), ('Q9', 'Qualität - Qualitätsrate (VDMA)'), ('Q10', 'Qualität - [kritischer] Maschinenfähigkeitssindex (VDMA)'), ('Q11', 'Qualität - [kritischer] Prozessfähigkeitsindex (VDMA)'), ('K1', 'Kosten/Nutzen - Wertschöpfungsquote (%)'), ('K2', 'Kosten/Nutzen - Fehlproduktionsquote (%)'), ('K3', 'Kosten/Nutzen - Abfallquote (%)'), ('K4', 'Kosten/Nutzen - Instandhaltungsquote (%)'), ('K5', 'Kosten/Nutzen - Return on Assets'), ('K6', 'Kosten/Nutzen - Overall Equipment Effectiveness (OEE)'), ('K7', 'Kosten/Nutzen - Net Equipment Effectiveness (NEE)'), ('K8', 'Kosten/Nutzen - Qualitätsrate (VDMA)'), ('K9', 'Kosten/Nutzen - Nutzgrad/Nutzungsgrad (VDMA)'), ('K10', 'Kosten/Nutzen - Technischer Nutzgrad (VDMA)'), ('K11', 'Kosten/Nutzen - Prozessgrad (VDMA)'), ('A1', 'Auslastung/Verfügbarkeit - Maschinenauslastung (%)'), ('A2', 'Auslastung/Verfügbarkeit - Stillstandszeit (h)'), ('A3', 'Auslastung/Verfügbarkeit - Maschinenausfallquote (%)'), ('A4', 'Auslastung/Verfügbarkeit - Mean Time between Failure (Tage)'), ('A5', 'Auslastung/Verfügbarkeit - Mean Time to Repair (Tage)'), ('A6', 'Auslastung/Verfügbarkeit - Anlagenverfügbarkeit (%)'), ('A7', 'Auslastung/Verfügbarkeit - Kapazitätauslastungsgrad (%)'), ('A8', 'Auslastung/Verfügbarkeit - Beleggrad (VDMA)'), ('A9', 'Auslastung/Verfügbarkeit - Belegnutzgrad (VDMA)'), ('F1', 'Flexibilität - Reaktionsfähigkeit auf Kundenwünsche'), ('F2', 'Flexibilität - Mindestlosgröße (Stk.)'), ('F3', 'Flexibilität - Lieferfähigkeit (%)'), ('F4', 'Flexibilität - Every Part Every Interval (Tage)'), ('F5', 'Mitarbeiter - Fehlzeiten (%)'), ('F6', 'Mitarbeiter - Mitarbeiterverfügbarkeit (%)'), ('F7', 'Mitarbeiter - Mitarbeitereffektivität (%)'), ('F8', 'Mitarbeiter - Beschäftigungsgrad (%)'), ('F9', 'Mitarbeiter - Mitarbeiterproduktivität'), ('L1', 'Logistik - Lagerdauer (Tage)'), ('L2', 'Logistik - Lieferzeit (Tage)'), ('L3', 'Logistik - Lagerumschlag (-)'), ('L4', 'Logistik - Bearbeitungszeit pro Anfrage (h)'), ('L5', 'Logistik - Lieferfähigkeit (%)')], help_text='Key Performance Indikator, der durch die Komponente optimiert werden soll;es sollte auf jeden Fall eine Kategorie ausgesucht werden (Wert); dies Auswahl kann über KPI-Verfeinerung noch verfeinert werden;', max_length=3, verbose_name='Typ')),
                ('technical_specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.use')),
            ],
            options={
                'verbose_name': 'KPI',
                'verbose_name_plural': 'KPI',
            },
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Erstellt')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('mail', models.EmailField(max_length=254, verbose_name='E-Mail-Adresse')),
                ('message', models.TextField(help_text='Ihre Nachricht an den Anbieter', max_length=2000, verbose_name='Nachricht')),
                ('component', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.component', verbose_name='KI Lösung')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Adressat')),
            ],
            options={
                'verbose_name': 'Anfrage',
                'verbose_name_plural': 'Anfragen',
            },
        ),
        migrations.CreateModel(
            name='HierarchyLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('IP', 'Intelligentes Produkt (product)'), ('FD', 'Feldebene/Sensoren/Aktoren (field device)'), ('CD', 'Regelung & Steuerung (control device)'), ('ST', 'Station/Maschine oder Maschinengruppe (station)'), ('WC', 'Technische Anlage (work center)'), ('EP', 'Unternehmen (enterprise)'), ('CW', 'Vernetze Welt (Connected World)')], help_text='Automatisierebene, für die die KI-Komponente gedacht ist', max_length=2)),
                ('application_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.applicationprofile')),
            ],
            options={
                'verbose_name': 'Hierarchie-Ebene',
                'verbose_name_plural': 'Hierarchie-Ebene',
            },
        ),
        migrations.CreateModel(
            name='DataAnalysisProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('DA', 'Datenerfassung'), ('DC', 'Data-Cleaning/Pre-processing'), ('DI', 'Datenintegration'), ('MS', 'Modellauswahl'), ('MT', 'Modellbildung & Training'), ('MA', 'Modellanalyse/erklärung'), ('MU', 'Modellanwendung'), ('VI', 'Visualisierung'), ('PC', 'KI-basierte Prozesssteuerung')], help_text='Unterstützte Phasen des Datenanalyse-Prozesses (z.B. Data Cleaning)', max_length=2)),
                ('technical_specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.technicalspecification')),
            ],
            options={
                'verbose_name': 'Datenanalyse-Prozess',
                'verbose_name_plural': 'Datenanalyse-Prozess',
            },
        ),
        migrations.CreateModel(
            name='CorporateDivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('CS', 'Kundendienst / Inbetriebnahme'), ('DD', 'Konstruktion / Entwicklung'), ('PA', 'Produktion / Montage'), ('MA', 'Instandhaltung'), ('LO', 'Logistik / Supply Chain Management'), ('MC', 'Marketing / Kommunikation'), ('MM', 'Materialwirtschaft / Einkauf'), ('AC', 'Rechnungswesen / Controlling'), ('CG', 'Management / Unternehmensführung'), ('SP', 'Sales / Preisgestaltung')], help_text='Bereich des produzierenden Unternehmens, für den die Komponenten entwickelt wurde', max_length=2)),
                ('application_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.applicationprofile')),
            ],
            options={
                'verbose_name': 'Unternehmensbereich',
                'verbose_name_plural': 'Unternehmensbereich',
            },
        ),
        migrations.CreateModel(
            name='BranchProven',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('C10', 'Herstellung von Nahrungs- und Futtermitteln (C.10)'), ('C11', 'Getränkeherstellung (C.11)'), ('C12', 'Tabakverarbeitung (C.12)'), ('C13', 'Herstellung von Textilien (C.13)'), ('C14', 'Herstellung von Bekleidung (C.14)'), ('C15', 'Herstellung von Leder, Lederwaren und Schuhen (C.15)'), ('C16', 'Herstellung von Holz-, Flecht-, Korb- und Korkwaren (ohne Möbel) (C.16)'), ('C17', 'Herstellung von Papier, Pappe und Waren daraus (C.17)'), ('C18', 'Herstellung von Druckerzeugnissen; Vervielfältigung von bespielten Ton-, Bild und Datenträgern (C.18)'), ('C19', 'Kokerei und Mineralölverarbeitung (C.19)'), ('C20', 'Herstellung von chemischen Erzeugnissen (C.20)'), ('C21', 'Herstellung von pharmazeutischen Erzeugnissen (C.21)'), ('C22', 'Herstellung von Gummi- und Kunststoffwaren (C.22)'), ('C23', 'Herstellung von Glas und Glaswaren, Keramik, Verarbeitung von Steinen und Erden (C.23)'), ('C24', 'Metallerzeugung und –bearbeitung (C.24)'), ('C25', 'Herstellung von Metallerzeugnissen (C.25)'), ('C26', 'Herstellung von Datenverarbeitungsgeräten, elektronischen und optischen Erzeugnissen (C.26)'), ('C27', 'Herstellung von elektrischen Ausrüstungen (C.27)'), ('C28', 'Maschinenbau (C.28)'), ('C29', 'Herstellung von Kraftwagen und Kraftwagenteilen (C.29)'), ('C30', 'Sonstiger Fahrzeugbau (C.30)'), ('C31', 'Herstellung von Möbeln (C.31)'), ('C32', 'Herstellung von sonstigen Waren (C.32)'), ('ALL', 'Keine / Branchenunabhängig')], help_text='Branche(n) für die die Komponente bereits erfolgreich erprobt wurde; belegte Anwendung', max_length=3)),
                ('application_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.applicationprofile')),
            ],
            options={
                'verbose_name': 'Branche (erprobt)',
                'verbose_name_plural': 'Branche (erprobt)',
            },
        ),
        migrations.CreateModel(
            name='BranchApplicable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('C10', 'Herstellung von Nahrungs- und Futtermitteln (C.10)'), ('C11', 'Getränkeherstellung (C.11)'), ('C12', 'Tabakverarbeitung (C.12)'), ('C13', 'Herstellung von Textilien (C.13)'), ('C14', 'Herstellung von Bekleidung (C.14)'), ('C15', 'Herstellung von Leder, Lederwaren und Schuhen (C.15)'), ('C16', 'Herstellung von Holz-, Flecht-, Korb- und Korkwaren (ohne Möbel) (C.16)'), ('C17', 'Herstellung von Papier, Pappe und Waren daraus (C.17)'), ('C18', 'Herstellung von Druckerzeugnissen; Vervielfältigung von bespielten Ton-, Bild und Datenträgern (C.18)'), ('C19', 'Kokerei und Mineralölverarbeitung (C.19)'), ('C20', 'Herstellung von chemischen Erzeugnissen (C.20)'), ('C21', 'Herstellung von pharmazeutischen Erzeugnissen (C.21)'), ('C22', 'Herstellung von Gummi- und Kunststoffwaren (C.22)'), ('C23', 'Herstellung von Glas und Glaswaren, Keramik, Verarbeitung von Steinen und Erden (C.23)'), ('C24', 'Metallerzeugung und –bearbeitung (C.24)'), ('C25', 'Herstellung von Metallerzeugnissen (C.25)'), ('C26', 'Herstellung von Datenverarbeitungsgeräten, elektronischen und optischen Erzeugnissen (C.26)'), ('C27', 'Herstellung von elektrischen Ausrüstungen (C.27)'), ('C28', 'Maschinenbau (C.28)'), ('C29', 'Herstellung von Kraftwagen und Kraftwagenteilen (C.29)'), ('C30', 'Sonstiger Fahrzeugbau (C.30)'), ('C31', 'Herstellung von Möbeln (C.31)'), ('C32', 'Herstellung von sonstigen Waren (C.32)'), ('ALL', 'Keine / Branchenunabhängig')], help_text='Branche, in denen die Komponenten anwendbar ist', max_length=3)),
                ('application_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.applicationprofile')),
            ],
            options={
                'verbose_name': 'Branche (anwendbar)',
                'verbose_name_plural': 'Branche (anwendbar)',
            },
        ),
        migrations.AddField(
            model_name='basedata',
            name='component',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalogue.component'),
        ),
        migrations.AddField(
            model_name='applicationprofile',
            name='component',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalogue.component'),
        ),
        migrations.CreateModel(
            name='AIMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Angabe der verwendeten KI-Methode (z.B. Deep Learning)', max_length=1000)),
                ('technical_specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.technicalspecification')),
            ],
            options={
                'verbose_name': 'KI-Methode',
                'verbose_name_plural': 'KI-Methode',
            },
        ),
    ]
