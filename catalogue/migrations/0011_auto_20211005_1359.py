# Generated by Django 3.2.7 on 2021-10-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0010_component_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchapplicable',
            name='name',
            field=models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('C10', 'Nahrungs- und Futtermittel'), ('C11', 'Getränke'), ('C12', 'Tabakverarbeitung'), ('C13', 'Textilien'), ('C14', 'Bekleidung'), ('C15', 'Leder, Lederwaren und Schuhe'), ('C16', 'Holz-, Flecht-, Korb- und Korkwaren (ohne Möbel)'), ('C17', 'Papier, Pappe und Waren daraus'), ('C18', 'Druckerzeugnisse; Vervielfältigung von bespielten Ton-, Bild und Datenträgern'), ('C19', 'Kokerei und Mineralölverarbeitung'), ('C20', 'Chemische Erzeugnisse'), ('C21', 'Pharmazeutischen Erzeugnisse'), ('C22', 'Gummi- und Kunststoffwaren'), ('C23', 'Glas und Glaswaren, Keramik, Verarbeitung von Steinen und Erden'), ('C24', 'Metallerzeugung und –bearbeitung'), ('C25', 'Metallerzeugnisse'), ('C26', 'Datenverarbeitungsgeräte, elektronische und optische Erzeugnisse'), ('C27', 'Elektrische Ausrüstungen'), ('C28', 'Maschinenbau'), ('C29', 'Kraftwagen und Kraftwagenteile'), ('C30', 'Sonstiger Fahrzeugbau'), ('C31', 'Möbel'), ('C32', 'Herstellung von sonstigen Waren'), ('ALL', 'Keine / Branchenunabhängig')], help_text='Branche, in denen die Lösungen anwendbar ist', max_length=3),
        ),
        migrations.AlterField(
            model_name='branchproven',
            name='name',
            field=models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('C10', 'Nahrungs- und Futtermittel'), ('C11', 'Getränke'), ('C12', 'Tabakverarbeitung'), ('C13', 'Textilien'), ('C14', 'Bekleidung'), ('C15', 'Leder, Lederwaren und Schuhe'), ('C16', 'Holz-, Flecht-, Korb- und Korkwaren (ohne Möbel)'), ('C17', 'Papier, Pappe und Waren daraus'), ('C18', 'Druckerzeugnisse; Vervielfältigung von bespielten Ton-, Bild und Datenträgern'), ('C19', 'Kokerei und Mineralölverarbeitung'), ('C20', 'Chemische Erzeugnisse'), ('C21', 'Pharmazeutischen Erzeugnisse'), ('C22', 'Gummi- und Kunststoffwaren'), ('C23', 'Glas und Glaswaren, Keramik, Verarbeitung von Steinen und Erden'), ('C24', 'Metallerzeugung und –bearbeitung'), ('C25', 'Metallerzeugnisse'), ('C26', 'Datenverarbeitungsgeräte, elektronische und optische Erzeugnisse'), ('C27', 'Elektrische Ausrüstungen'), ('C28', 'Maschinenbau'), ('C29', 'Kraftwagen und Kraftwagenteile'), ('C30', 'Sonstiger Fahrzeugbau'), ('C31', 'Möbel'), ('C32', 'Herstellung von sonstigen Waren'), ('ALL', 'Keine / Branchenunabhängig')], help_text='Branche(n) für die die Lösung bereits erfolgreich erprobt wurde; belegte Anwendung', max_length=3),
        ),
        migrations.AlterField(
            model_name='component',
            name='additional_info',
            field=models.TextField(blank=True, help_text='Zusatzinformation zur Lösung', verbose_name='Zusatzinformationen'),
        ),
        migrations.AlterField(
            model_name='component',
            name='data_formats',
            field=models.CharField(blank=True, help_text='Datenformate, die von der KI-Lösung verarbeitet werden können und Datenformat der Ergebnisse', max_length=1000, verbose_name='Datenformate'),
        ),
        migrations.AlterField(
            model_name='component',
            name='description',
            field=models.TextField(help_text='Kurze Beschreibung der Lösung', verbose_name='Kurzbeschreibung'),
        ),
        migrations.AlterField(
            model_name='component',
            name='devices',
            field=models.CharField(help_text='Maschinen und IoT Devices, mit denen die Lösung kompatibel ist', max_length=1000, verbose_name='Maschinen/Steuerungen'),
        ),
        migrations.AlterField(
            model_name='component',
            name='hardware_requirements',
            field=models.CharField(help_text='Spezielle Hardware, welche für den Betrieb der Lösung notwendig ist (z.B. Kamera, Roboter)', max_length=1000, verbose_name='Spezielle Hardware'),
        ),
        migrations.AlterField(
            model_name='component',
            name='it_environment',
            field=models.CharField(help_text='Anforderungen an die IT-Umgebung (inkl. IT Hardware) und an weitere Software/Bibliotheken, die für den Betrieb der Lösung notwendig sind', max_length=1000, verbose_name='IT Umgebung/Software'),
        ),
        migrations.AlterField(
            model_name='component',
            name='manufacturer',
            field=models.CharField(help_text='Entwickler und/oder Hersteller der Lösung', max_length=1000, verbose_name='Hersteller'),
        ),
        migrations.AlterField(
            model_name='component',
            name='name',
            field=models.CharField(help_text='Bezeichnung der Lösung', max_length=200, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='component',
            name='realtime_processing',
            field=models.IntegerField(choices=[(None, 'Bitte Wert auswählen'), (0, 'Keine Echtzeit'), (1, 'Weiche Echtzeit'), (2, 'Harte Echtzeit'), (3, 'Feste Echtzeit')], help_text='Klassifizierung der Lösung in Bezug auf ihre Echtzeitfähigkeit', verbose_name='Echtzeitverarbeitung'),
        ),
        migrations.AlterField(
            model_name='component',
            name='scenarios',
            field=models.TextField(help_text='Beschreibung von Szenarien, in denen die Lösung bereits erfolgreich eingesetzt wurde', verbose_name='Szenarien / Use cases'),
        ),
        migrations.AlterField(
            model_name='component',
            name='trl',
            field=models.IntegerField(choices=[(None, 'Bitte Wert auswählen'), (1, 'TRL 1 - Grundprinzipien beobachtet'), (2, 'TRL 2 - Technologiekonzept formuliert'), (3, 'TRL 3 - Experimenteller Nachweis des Konzepts'), (4, 'TRL 4 - Technologie im Labor überprüft'), (5, 'TRL 5 - Technologie in relevanter Umgebung überprüft'), (6, 'TRL 6 - Technologie in relevanter Umgebung getestet'), (7, 'TRL 7 - Test eines System-Prototyps im realen Einsatz'), (8, 'TRL 8 - System ist komplett und qualifiziert'), (9, 'TRL 9 - System funktioniert in operationeller Umgebung')], help_text='Status der Lösung in Bezug auf Ihre Einsetzbarkeit durch die Angabe eines Technischen Reifegrades (Technology Readiness Level).', verbose_name='TRL'),
        ),
        migrations.AlterField(
            model_name='corporatedivision',
            name='name',
            field=models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('CS', 'Kundendienst / Inbetriebnahme'), ('DD', 'Konstruktion / Entwicklung'), ('PA', 'Produktion / Montage'), ('MA', 'Instandhaltung'), ('LO', 'Logistik / Supply Chain Management'), ('MC', 'Marketing / Kommunikation'), ('MM', 'Materialwirtschaft / Einkauf'), ('AC', 'Rechnungswesen / Controlling'), ('CG', 'Management / Unternehmensführung'), ('SP', 'Sales / Preisgestaltung')], help_text='Bereich des produzierenden Unternehmens, für den die Lösungen entwickelt wurde', max_length=2),
        ),
        migrations.AlterField(
            model_name='hierarchylevel',
            name='name',
            field=models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('IP', 'Intelligentes Produkt (product)'), ('FD', 'Feldebene/Sensoren/Aktoren (field device)'), ('CD', 'Regelung & Steuerung (control device)'), ('ST', 'Station/Maschine oder Maschinengruppe (station)'), ('WC', 'Technische Anlage (work center)'), ('EP', 'Unternehmen (enterprise)'), ('CW', 'Vernetze Welt (Connected World)')], help_text='Automatisierebene, für die die KI-Lösung gedacht ist', max_length=2),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='type',
            field=models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('E1', 'Effizienz - Bearbeitungszeit pro Anfrage (h)'), ('E2', 'Effizienz - Termintreue (%)'), ('E3', 'Effizienz - Rüstzeitanteil (%)'), ('E4', 'Effizienz - Automatisierungsgrad (%)'), ('E5', 'Effizienz - Durchlaufzeit (Tage)'), ('E6', 'Effizienz - Durchsatz (VDMA)'), ('E7', 'Effizienz - Produktionsvolumen/Zählwert'), ('E8', 'Effizienz - Stillstandzeit/Anzahl und Dauer ungeplanter Produktionsausfälle'), ('E9', 'Effizienz - Taktrate'), ('E10', 'Effizienz - Taktzeit'), ('Q1', 'Qualität - Qualitätsmängel'), ('Q2', 'Qualität - Rückgabequote'), ('Q3', 'Qualität - Right first Time/ Nacharbeitsquote / First Pass Yield (FPY, VDMA)'), ('Q4', 'Qualität - Fall-off-rate (VDMA)'), ('Q5', 'Qualität - Reklamationsquote (%)'), ('Q6', 'Qualität - Ausschussquote (%) / Ausschussgrad (VDMA)'), ('Q7', 'Qualität - Qualitätsgrad (%)'), ('Q8', 'Qualität - Fehlproduktionsquote (%)'), ('Q9', 'Qualität - Qualitätsrate (VDMA)'), ('Q10', 'Qualität - [kritischer] Maschinenfähigkeitssindex (VDMA)'), ('Q11', 'Qualität - [kritischer] Prozessfähigkeitsindex (VDMA)'), ('K1', 'Kosten/Nutzen - Wertschöpfungsquote (%)'), ('K2', 'Kosten/Nutzen - Fehlproduktionsquote (%)'), ('K3', 'Kosten/Nutzen - Abfallquote (%)'), ('K4', 'Kosten/Nutzen - Instandhaltungsquote (%)'), ('K5', 'Kosten/Nutzen - Return on Assets'), ('K6', 'Kosten/Nutzen - Overall Equipment Effectiveness (OEE)'), ('K7', 'Kosten/Nutzen - Net Equipment Effectiveness (NEE)'), ('K8', 'Kosten/Nutzen - Qualitätsrate (VDMA)'), ('K9', 'Kosten/Nutzen - Nutzgrad/Nutzungsgrad (VDMA)'), ('K10', 'Kosten/Nutzen - Technischer Nutzgrad (VDMA)'), ('K11', 'Kosten/Nutzen - Prozessgrad (VDMA)'), ('A1', 'Auslastung/Verfügbarkeit - Maschinenauslastung (%)'), ('A2', 'Auslastung/Verfügbarkeit - Stillstandszeit (h)'), ('A3', 'Auslastung/Verfügbarkeit - Maschinenausfallquote (%)'), ('A4', 'Auslastung/Verfügbarkeit - Mean Time between Failure (Tage)'), ('A5', 'Auslastung/Verfügbarkeit - Mean Time to Repair (Tage)'), ('A6', 'Auslastung/Verfügbarkeit - Anlagenverfügbarkeit (%)'), ('A7', 'Auslastung/Verfügbarkeit - Kapazitätauslastungsgrad (%)'), ('A8', 'Auslastung/Verfügbarkeit - Beleggrad (VDMA)'), ('A9', 'Auslastung/Verfügbarkeit - Belegnutzgrad (VDMA)'), ('F1', 'Flexibilität - Reaktionsfähigkeit auf Kundenwünsche'), ('F2', 'Flexibilität - Mindestlosgröße (Stk.)'), ('F3', 'Flexibilität - Lieferfähigkeit (%)'), ('F4', 'Flexibilität - Every Part Every Interval (Tage)'), ('F5', 'Mitarbeiter - Fehlzeiten (%)'), ('F6', 'Mitarbeiter - Mitarbeiterverfügbarkeit (%)'), ('F7', 'Mitarbeiter - Mitarbeitereffektivität (%)'), ('F8', 'Mitarbeiter - Beschäftigungsgrad (%)'), ('F9', 'Mitarbeiter - Mitarbeiterproduktivität'), ('L1', 'Logistik - Lagerdauer (Tage)'), ('L2', 'Logistik - Lieferzeit (Tage)'), ('L3', 'Logistik - Lagerumschlag (-)'), ('L4', 'Logistik - Bearbeitungszeit pro Anfrage (h)'), ('L5', 'Logistik - Lieferfähigkeit (%)')], help_text='Key Performance Indikator, der durch die Lösung optimiert werden soll;es sollte auf jeden Fall eine Kategorie ausgesucht werden (Wert); dies Auswahl kann über KPI-Verfeinerung noch verfeinert werden;', max_length=3, verbose_name='Typ'),
        ),
        migrations.AlterField(
            model_name='licenses',
            name='type',
            field=models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('FW', 'Freeware'), ('OSCL', 'Open Source / copy left'), ('OS', 'Open Source / no copy left'), ('PRO', 'Proprietär')], help_text='Welche Lizenzen bringt die Lösung mit, insbesondere Open Source Lizenzen', max_length=4, verbose_name='Typ'),
        ),
        migrations.AlterField(
            model_name='process',
            name='name',
            field=models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('PD', 'Produktionsentwicklung'), ('PA', 'Fertigungs- und Montagevorbereitung'), ('PP', 'Produktionsplanung und –steuerung'), ('PM', 'Teilefertigung'), ('PMPP', 'Teilefertigung - Produktionsprozess (Prozesskette)'), ('PMSP', 'Teilefertigung - Einzelfertigungsprozess'), ('AS', 'Montage, (VDI 2860)'), ('QA', 'Qualitätssicherung'), ('MFL', 'Materialfluss, Logistik'), ('CP', 'Änderungsprozesse'), ('PRODM', 'Produktionsinstandhaltung')], help_text='Prozess der durch die KI-Lösung unterstützt wird', max_length=5),
        ),
        migrations.AlterField(
            model_name='report',
            name='message',
            field=models.TextField(help_text='Ihre Nachricht', max_length=2000, verbose_name='Warum möchten Sie diese Lösung melden?'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(blank=True, choices=[(None, 'Bitte Wert auswählen'), ('PMCM', 'Predictive Maintenance/Condition Monitoring'), ('QCM', 'Qualitätskontrolle und –management'), ('OPP', 'Optimierte Prozessplanung'), ('OPC', 'Optimierte Prozesssteuerung'), ('RAS', 'Robotik & autonome Systeme'), ('IST', 'Intelligente Sensorik'), ('KM', 'Wissensmanagement'), ('FPA', 'Vorhersagen und Predictive Analytics'), ('ORS', 'Optimiertes Ressourcenmanagement'), ('IA', 'Intelligente Automatisierung'), ('IAS', 'Intelligente Assistenzsysteme'), ('DA', 'Datenanalyse'), ('DM', 'Data Management'), ('VAR', 'Virtuelle und erweiterte Realität'), ('OTHER', 'Sonstiges')], help_text='Art der Aufgabe, der die beschriebene KI-Lösung zugeordnet werden kann (z.B. Predictive Maintenance, Qualitätsprüfung))', max_length=5),
        ),
    ]
