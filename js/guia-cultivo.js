/* ==========================================================================
   CannaCulture • Guía de Cultivo (guia-cultivo.html) — v208
   Selector reactivo ES / EN / DE / IT sin recarga + navegación por etapas.
   El idioma se comparte con el kiosco mediante localStorage('kiosk_lang').
   ========================================================================== */
(function () {
  'use strict';

  const STAGE_ICONS = ['🌰', '🌿', '🌸', '🔬', '🫙'];
  const SUPPORTED = ['es', 'en', 'de', 'it'];

  const I18N = {
    /* ============================== ESPAÑOL ============================== */
    es: {
      meta: {
        title: 'Guía de Cultivo en 5 Etapas • CannaCulture',
        description: 'Guía de cultivo interactiva: germinación, vegetativo, floración, cosecha por tricomas, secado y curado.'
      },
      nav: { catalog: 'Catálogo', guide: 'Guía de Cultivo', dispensary: 'Dispensario CSC' },
      hero: {
        eyebrow: 'Guía práctica · 5 etapas',
        title: 'Guía de Cultivo',
        subtitle: 'De la semilla al bote: todo el ciclo explicado paso a paso, con los parámetros que de verdad importan.'
      },
      ui: {
        prev: 'Anterior', next: 'Siguiente', stage: 'Etapa', of: 'de',
        params: 'Parámetros clave', steps: 'Paso a paso', tip: '💡 Consejo clave',
        trichomes: 'Lectura de tricomas', fix: 'Solución:'
      },
      stages: [
        {
          short: 'Germinación',
          title: 'Germinación & Plántula',
          duration: '3–10 días + 2 semanas',
          summary: 'La semilla despierta. Humedad constante, oscuridad y mucha delicadeza: es la etapa más frágil del ciclo.',
          params: [
            ['🌡️', 'Temperatura', '22–25 °C'],
            ['💧', 'Humedad', '70–80 % HR'],
            ['🧪', 'pH del agua', '6.0 – 6.5'],
            ['🌑', 'Luz', 'Oscuridad → luz suave']
          ],
          steps: [
            'Coloca las semillas entre dos <strong>servilletas de papel húmedas</strong> (no encharcadas) dentro de un plato tapado, en un lugar <strong>oscuro y templado</strong>.',
            'Revisa cada 12 h: cuando la raíz principal (radícula) asome <strong>0,5–1 cm</strong>, es el momento de trasplantar.',
            'Trasplanta con cuidado a un sustrato ligero tipo <strong>Light Mix</strong>, con la raíz hacia abajo a 0,5–1 cm de profundidad y sin tocar la radícula.',
            '<strong>Primeros riegos mínimos:</strong> pulveriza o riega un pequeño círculo alrededor del tallo. Las raíces jóvenes necesitan oxígeno, no un charco.',
            'Usa agua con <strong>pH 6.0–6.5</strong> y sin fertilizantes: el Light Mix aporta lo necesario durante las primeras semanas.'
          ],
          tip: 'Menos es más: el exceso de agua es la primera causa de muerte de plántulas (damping-off).'
        },
        {
          short: 'Vegetativo',
          title: 'Crecimiento Vegetativo',
          duration: '3–8 semanas',
          summary: 'La planta construye su estructura: raíces, tallos y hojas. Aquí se define el potencial de la cosecha.',
          params: [
            ['💡', 'Fotoperiodo', '18 h luz / 6 h oscuridad'],
            ['🌡️', 'Temperatura', '22–28 °C'],
            ['💧', 'Humedad', '55–70 % HR'],
            ['⚗️', 'Nutrición', 'Nitrógeno (N) suave']
          ],
          steps: [
            'Mantén un fotoperiodo de <strong>18/6</strong> (18 h de luz y 6 h de oscuridad) para que la planta permanezca en fase vegetativa.',
            '<strong>Regla de oro del riego:</strong> levanta la maceta. Riega solo cuando pese claramente poco; ese ciclo húmedo-seco <strong>oxigena las raíces</strong> y las estimula a crecer.',
            'Riega hasta obtener un 10–20 % de drenaje y deja que el sustrato se seque antes del siguiente riego.',
            'Introduce un fertilizante de crecimiento con <strong>aporte suave de nitrógeno</strong>, empezando a 1/4–1/2 de la dosis del fabricante.',
            'Trasplanta a una maceta mayor cuando las raíces ocupen el contenedor y mantén ventilación constante para fortalecer los tallos.'
          ],
          tip: 'Hojas de verde intenso y sanas = nitrógeno correcto. Puntas quemadas = te estás pasando: reduce la dosis.'
        },
        {
          short: 'Floración',
          title: 'Floración',
          duration: '8–10 semanas',
          summary: 'La planta deja de estirarse y concentra toda su energía en producir flores densas y resinosas.',
          params: [
            ['💡', 'Fotoperiodo', '12 h luz / 12 h oscuridad'],
            ['🌡️', 'Temperatura', '20–26 °C'],
            ['💧', 'Humedad', '40–50 % HR'],
            ['⚗️', 'Nutrición', 'Fósforo (P) + Potasio (K)']
          ],
          steps: [
            'En variedades <strong>fotodependientes</strong>, cambia a <strong>12/12</strong> para inducir la floración. Las autoflorecientes florecen solas sin cambiar el fotoperiodo.',
            'Respeta la <strong>oscuridad total</strong>: cualquier fuga de luz durante las 12 h nocturnas estresa la planta y puede provocar hermafroditismo.',
            'Baja progresivamente la humedad hasta el <strong>40–50 % HR</strong> para evitar <strong>botrytis</strong> (podredumbre del cogollo) y <strong>oídio</strong>.',
            'Cambia a un fertilizante de floración rico en <strong>fósforo y potasio</strong> y reduce el nitrógeno.',
            'Asegura buena circulación de aire entre cogollos y revisa a diario el interior de las flores más densas.'
          ],
          tip: 'En las primeras 2–3 semanas la planta puede duplicar su altura (stretch): deja espacio suficiente hasta la luz.'
        },
        {
          short: 'Cosecha',
          title: 'Punto Óptimo de Cosecha',
          duration: 'Ventana de 1–2 semanas',
          summary: 'No cortes por calendario: cosecha por tricomas. Un microscopio de bolsillo es tu mejor herramienta.',
          params: [
            ['🔬', 'Herramienta', 'Microscopio 60x–100x'],
            ['🎯', 'Dónde mirar', 'Cogollos, no hojas'],
            ['🚿', 'Lavado de raíces', '7–14 días antes'],
            ['⏱️', 'Revisión', 'Cada 1–2 días']
          ],
          trichomes: [
            ['clear', 'Transparentes', 'Inmaduro: potencia baja. Aún no es el momento.'],
            ['milky', 'Lechosos', 'Pico de THC: efecto más cerebral y potente.'],
            ['amber', 'Ámbar', 'Efecto corporal y sedante: el THC empieza a degradarse.']
          ],
          steps: [
            'Observa los tricomas de las <strong>flores</strong> (no de las hojas de azúcar, que maduran antes) con el microscopio.',
            '<strong>Mayoría lechosos con 10–20 % ámbar</strong> = equilibrio clásico entre potencia y efecto corporal.',
            'Si buscas un efecto más relajante y sedante, espera a un <strong>30 % o más de ámbar</strong>.',
            'Los pistilos marrones son solo orientativos: los <strong>tricomas</strong> son el indicador fiable.'
          ],
          tip: 'Las prisas en la última semana cuestan potencia, sabor y peso. Confírmalo siempre con la lupa.'
        },
        {
          short: 'Secado & Curado',
          title: 'Secado & Curado',
          duration: '10–14 días + 2–8 semanas',
          summary: 'El paso que diferencia una flor correcta de una excelente: sabor, aroma y suavidad.',
          params: [
            ['🌑', 'Ambiente', 'Oscuridad total'],
            ['🌡️', 'Temperatura', '18–20 °C'],
            ['💧', 'Humedad', '50–55 % HR'],
            ['🫙', 'Curado', 'Botes herméticos']
          ],
          steps: [
            'Cuelga las ramas boca abajo en un espacio en <strong>oscuridad</strong>, con ventilación suave e indirecta (nunca un ventilador apuntando a las flores).',
            'Mantén <strong>18–20 °C y 50–55 % HR durante 10–14 días</strong>. Un secado lento preserva los terpenos.',
            'Está listo cuando los tallos pequeños se parten con un chasquido en lugar de doblarse.',
            'Manicura y guarda las flores en <strong>botes de cristal herméticos</strong>, llenos al 70–75 %.',
            '<strong>Ventila los botes a diario</strong> (10–15 min) durante las 2 primeras semanas; después, una vez por semana.'
          ],
          tip: 'Si al abrir el bote huele a amoníaco, la flor está demasiado húmeda: déjala airear unas horas antes de volver a cerrarlo.'
        }
      ],
      errors: {
        title: '⚠️ 3 Errores Clásicos de Principiante a Evitar',
        items: [
          ['💦', 'Encharcamiento por exceso de riego', 'Regar "por si acaso" ahoga las raíces: sin oxígeno se pudren y la planta se ve caída aunque le sobre agua.', 'riega según el peso de la maceta y asegura un buen drenaje.'],
          ['🧪', 'Sobrefertilización temprana', 'Las plántulas no necesitan abono. Fertilizar demasiado pronto quema puntas y raíces y bloquea nutrientes.', 'empieza en vegetativo con 1/4 de la dosis y sube poco a poco.'],
          ['⏳', 'Cosechar con prisas', 'Cortar con tricomas transparentes significa menos potencia, peor sabor y menos peso final.', 'usa la lupa y espera a que la mayoría de tricomas sean lechosos.']
        ]
      },
      footer: {
        disclaimer: 'Contenido divulgativo para personas adultas (18+). Infórmate y cumple la legislación vigente en tu país sobre el autocultivo.',
        back: 'Volver al Catálogo'
      }
    },

    /* ============================== ENGLISH ============================== */
    en: {
      meta: {
        title: '5-Stage Grow Guide • CannaCulture',
        description: 'Interactive grow guide: germination, vegetative, flowering, trichome-based harvest, drying and curing.'
      },
      nav: { catalog: 'Catalog', guide: 'Grow Guide', dispensary: 'CSC Dispensary' },
      hero: {
        eyebrow: 'Practical guide · 5 stages',
        title: 'Grow Guide',
        subtitle: 'From seed to jar: the whole cycle explained step by step, with the parameters that really matter.'
      },
      ui: {
        prev: 'Previous', next: 'Next', stage: 'Stage', of: 'of',
        params: 'Key parameters', steps: 'Step by step', tip: '💡 Key tip',
        trichomes: 'Reading trichomes', fix: 'Fix:'
      },
      stages: [
        {
          short: 'Germination',
          title: 'Germination & Seedling',
          duration: '3–10 days + 2 weeks',
          summary: 'The seed wakes up. Constant moisture, darkness and a gentle touch: this is the most fragile stage of the cycle.',
          params: [
            ['🌡️', 'Temperature', '22–25 °C'],
            ['💧', 'Humidity', '70–80 % RH'],
            ['🧪', 'Water pH', '6.0 – 6.5'],
            ['🌑', 'Light', 'Darkness → soft light']
          ],
          steps: [
            'Place the seeds between two <strong>damp paper towels</strong> (not soaked) inside a covered plate, somewhere <strong>dark and warm</strong>.',
            'Check every 12 h: once the taproot (radicle) is <strong>0.5–1 cm</strong> long, it is time to transplant.',
            'Carefully transplant into a light substrate such as <strong>Light Mix</strong>, root facing down, 0.5–1 cm deep, without touching the radicle.',
            '<strong>Minimal first waterings:</strong> mist or water a small circle around the stem. Young roots need oxygen, not a puddle.',
            'Use water at <strong>pH 6.0–6.5</strong> with no fertilizer: Light Mix provides everything needed for the first weeks.'
          ],
          tip: 'Less is more: overwatering is the number one cause of seedling death (damping-off).'
        },
        {
          short: 'Vegetative',
          title: 'Vegetative Growth',
          duration: '3–8 weeks',
          summary: 'The plant builds its structure: roots, stems and leaves. This is where the harvest potential is defined.',
          params: [
            ['💡', 'Photoperiod', '18 h light / 6 h dark'],
            ['🌡️', 'Temperature', '22–28 °C'],
            ['💧', 'Humidity', '55–70 % RH'],
            ['⚗️', 'Nutrition', 'Gentle nitrogen (N)']
          ],
          steps: [
            'Keep an <strong>18/6</strong> photoperiod (18 h light, 6 h dark) so the plant stays in the vegetative phase.',
            '<strong>Golden watering rule:</strong> lift the pot. Water only when it feels clearly light; that wet-dry cycle <strong>oxygenates the roots</strong> and drives them to grow.',
            'Water until you get 10–20 % runoff and let the substrate dry out before the next watering.',
            'Introduce a grow fertilizer with a <strong>gentle nitrogen supply</strong>, starting at 1/4–1/2 of the manufacturer’s dose.',
            'Transplant to a bigger pot once roots fill the container and keep constant airflow to strengthen the stems.'
          ],
          tip: 'Deep green, healthy leaves = correct nitrogen. Burnt tips = you are overdoing it: lower the dose.'
        },
        {
          short: 'Flowering',
          title: 'Flowering',
          duration: '8–10 weeks',
          summary: 'The plant stops stretching and focuses all its energy on producing dense, resinous flowers.',
          params: [
            ['💡', 'Photoperiod', '12 h light / 12 h dark'],
            ['🌡️', 'Temperature', '20–26 °C'],
            ['💧', 'Humidity', '40–50 % RH'],
            ['⚗️', 'Nutrition', 'Phosphorus (P) + Potassium (K)']
          ],
          steps: [
            'For <strong>photoperiod</strong> strains, switch to <strong>12/12</strong> to trigger flowering. Autoflowers bloom on their own without changing the light cycle.',
            'Respect <strong>total darkness</strong>: any light leak during the 12-hour night stresses the plant and can cause hermaphroditism.',
            'Gradually lower humidity to <strong>40–50 % RH</strong> to prevent <strong>botrytis</strong> (bud rot) and <strong>powdery mildew</strong>.',
            'Switch to a bloom fertilizer rich in <strong>phosphorus and potassium</strong> and reduce nitrogen.',
            'Ensure good airflow between buds and inspect the inside of the densest flowers daily.'
          ],
          tip: 'During the first 2–3 weeks the plant can double its height (stretch): leave enough room below the light.'
        },
        {
          short: 'Harvest',
          title: 'Optimal Harvest Point',
          duration: '1–2 week window',
          summary: 'Don’t harvest by calendar: harvest by trichomes. A pocket microscope is your best tool.',
          params: [
            ['🔬', 'Tool', '60x–100x microscope'],
            ['🎯', 'Where to look', 'Buds, not leaves'],
            ['🚿', 'Root flush', '7–14 days before'],
            ['⏱️', 'Check', 'Every 1–2 days']
          ],
          trichomes: [
            ['clear', 'Clear', 'Immature: low potency. Not ready yet.'],
            ['milky', 'Milky', 'THC peak: the most cerebral and potent effect.'],
            ['amber', 'Amber', 'Body and sedative effect: THC starts to degrade.']
          ],
          steps: [
            'Inspect the trichomes on the <strong>flowers</strong> (not the sugar leaves, which mature earlier) under the microscope.',
            '<strong>Mostly milky with 10–20 % amber</strong> = the classic balance between potency and body effect.',
            'For a more relaxing, sedative effect, wait for <strong>30 % amber or more</strong>.',
            'Brown pistils are only a rough guide: <strong>trichomes</strong> are the reliable indicator.'
          ],
          tip: 'Rushing the last week costs potency, flavour and weight. Always confirm with the loupe.'
        },
        {
          short: 'Drying & Curing',
          title: 'Drying & Curing',
          duration: '10–14 days + 2–8 weeks',
          summary: 'The step that separates a decent flower from an excellent one: flavour, aroma and smoothness.',
          params: [
            ['🌑', 'Environment', 'Total darkness'],
            ['🌡️', 'Temperature', '18–20 °C'],
            ['💧', 'Humidity', '50–55 % RH'],
            ['🫙', 'Curing', 'Airtight jars']
          ],
          steps: [
            'Hang branches upside down in a <strong>dark</strong> space with gentle, indirect airflow (never a fan pointed at the flowers).',
            'Keep <strong>18–20 °C and 50–55 % RH for 10–14 days</strong>. A slow dry preserves terpenes.',
            'It is ready when small stems snap instead of bending.',
            'Trim and store the flowers in <strong>airtight glass jars</strong>, filled to 70–75 %.',
            '<strong>Burp the jars daily</strong> (10–15 min) for the first 2 weeks; after that, once a week.'
          ],
          tip: 'If the jar smells of ammonia when opened, the flower is too moist: let it air out for a few hours before sealing again.'
        }
      ],
      errors: {
        title: '⚠️ 3 Classic Beginner Mistakes to Avoid',
        items: [
          ['💦', 'Waterlogging from overwatering', 'Watering “just in case” drowns the roots: without oxygen they rot and the plant droops even with plenty of water.', 'water by the weight of the pot and ensure good drainage.'],
          ['🧪', 'Early overfeeding', 'Seedlings don’t need fertilizer. Feeding too early burns tips and roots and locks out nutrients.', 'start in veg at 1/4 dose and increase gradually.'],
          ['⏳', 'Harvesting in a hurry', 'Cutting with clear trichomes means less potency, worse flavour and lower final weight.', 'use the loupe and wait until most trichomes are milky.']
        ]
      },
      footer: {
        disclaimer: 'Educational content for adults (18+). Get informed and comply with your country’s laws on home growing.',
        back: 'Back to Catalog'
      }
    },

    /* ============================== DEUTSCH ============================== */
    de: {
      meta: {
        title: 'Anbau-Leitfaden in 5 Phasen • CannaCulture',
        description: 'Interaktiver Anbau-Leitfaden: Keimung, Wachstum, Blüte, Ernte nach Trichomen, Trocknung und Curing.'
      },
      nav: { catalog: 'Katalog', guide: 'Anbau-Leitfaden', dispensary: 'CSC-Ausgabe' },
      hero: {
        eyebrow: 'Praxis-Leitfaden · 5 Phasen',
        title: 'Anbau-Leitfaden',
        subtitle: 'Vom Samen bis ins Glas: der gesamte Zyklus Schritt für Schritt erklärt – mit den Werten, auf die es wirklich ankommt.'
      },
      ui: {
        prev: 'Zurück', next: 'Weiter', stage: 'Phase', of: 'von',
        params: 'Wichtige Parameter', steps: 'Schritt für Schritt', tip: '💡 Profi-Tipp',
        trichomes: 'Trichome richtig lesen', fix: 'Lösung:'
      },
      stages: [
        {
          short: 'Keimung',
          title: 'Keimung & Sämling',
          duration: '3–10 Tage + 2 Wochen',
          summary: 'Der Samen erwacht. Konstante Feuchtigkeit, Dunkelheit und viel Fingerspitzengefühl: die empfindlichste Phase des Zyklus.',
          params: [
            ['🌡️', 'Temperatur', '22–25 °C'],
            ['💧', 'Luftfeuchtigkeit', '70–80 % rLF'],
            ['🧪', 'pH-Wert Wasser', '6,0 – 6,5'],
            ['🌑', 'Licht', 'Dunkelheit → sanftes Licht']
          ],
          steps: [
            'Lege die Samen zwischen zwei <strong>feuchte Küchentücher</strong> (nicht triefnass) auf einen abgedeckten Teller, an einen <strong>dunklen, warmen</strong> Ort.',
            'Alle 12 h kontrollieren: Sobald die Keimwurzel <strong>0,5–1 cm</strong> lang ist, wird umgepflanzt.',
            'Vorsichtig in ein leichtes Substrat wie <strong>Light Mix</strong> setzen – Wurzel nach unten, 0,5–1 cm tief, ohne die Keimwurzel zu berühren.',
            '<strong>Minimale erste Bewässerung:</strong> sprühen oder einen kleinen Kreis um den Stiel gießen. Junge Wurzeln brauchen Sauerstoff, keine Pfütze.',
            'Wasser mit <strong>pH 6,0–6,5</strong> und ohne Dünger verwenden: Light Mix liefert in den ersten Wochen alles Nötige.'
          ],
          tip: 'Weniger ist mehr: Überwässerung ist die häufigste Todesursache bei Sämlingen (Umfallkrankheit).'
        },
        {
          short: 'Wachstum',
          title: 'Vegetatives Wachstum',
          duration: '3–8 Wochen',
          summary: 'Die Pflanze baut ihr Gerüst auf: Wurzeln, Stängel und Blätter. Hier entscheidet sich das Ertragspotenzial.',
          params: [
            ['💡', 'Lichtzyklus', '18 h Licht / 6 h Dunkel'],
            ['🌡️', 'Temperatur', '22–28 °C'],
            ['💧', 'Luftfeuchtigkeit', '55–70 % rLF'],
            ['⚗️', 'Nährstoffe', 'Sanft Stickstoff (N)']
          ],
          steps: [
            'Halte einen <strong>18/6</strong>-Lichtzyklus (18 h Licht, 6 h Dunkelheit) ein, damit die Pflanze in der Wachstumsphase bleibt.',
            '<strong>Goldene Gießregel:</strong> Topf anheben. Erst gießen, wenn er deutlich leicht ist – der Wechsel von nass und trocken <strong>versorgt die Wurzeln mit Sauerstoff</strong> und regt ihr Wachstum an.',
            'Gießen, bis 10–20 % Drainagewasser austreten, und das Substrat vor dem nächsten Gießen abtrocknen lassen.',
            'Wachstumsdünger mit <strong>sanfter Stickstoffgabe</strong> einführen, beginnend mit 1/4–1/2 der Herstellerdosis.',
            'In einen größeren Topf umtopfen, sobald die Wurzeln den Behälter ausfüllen, und für ständige Luftbewegung sorgen, um die Stängel zu stärken.'
          ],
          tip: 'Sattgrüne, gesunde Blätter = Stickstoff passt. Verbrannte Spitzen = zu viel: Dosis reduzieren.'
        },
        {
          short: 'Blüte',
          title: 'Blütephase',
          duration: '8–10 Wochen',
          summary: 'Die Pflanze hört auf zu strecken und steckt ihre ganze Energie in dichte, harzige Blüten.',
          params: [
            ['💡', 'Lichtzyklus', '12 h Licht / 12 h Dunkel'],
            ['🌡️', 'Temperatur', '20–26 °C'],
            ['💧', 'Luftfeuchtigkeit', '40–50 % rLF'],
            ['⚗️', 'Nährstoffe', 'Phosphor (P) + Kalium (K)']
          ],
          steps: [
            'Bei <strong>photoperiodischen</strong> Sorten auf <strong>12/12</strong> umstellen, um die Blüte einzuleiten. Autoflowering-Sorten blühen von selbst, ohne Änderung des Lichtzyklus.',
            '<strong>Absolute Dunkelheit</strong> einhalten: Jedes Lichtleck während der 12-stündigen Nacht stresst die Pflanze und kann Zwitterbildung auslösen.',
            'Luftfeuchtigkeit schrittweise auf <strong>40–50 % rLF</strong> senken, um <strong>Botrytis</strong> (Blütenfäule) und <strong>Mehltau</strong> zu vermeiden.',
            'Auf Blühdünger mit viel <strong>Phosphor und Kalium</strong> wechseln und Stickstoff reduzieren.',
            'Für gute Luftzirkulation zwischen den Buds sorgen und das Innere der dichtesten Blüten täglich kontrollieren.'
          ],
          tip: 'In den ersten 2–3 Wochen kann sich die Höhe der Pflanze verdoppeln (Stretch): genug Abstand zur Lampe lassen.'
        },
        {
          short: 'Ernte',
          title: 'Optimaler Erntezeitpunkt',
          duration: 'Zeitfenster von 1–2 Wochen',
          summary: 'Nicht nach Kalender ernten, sondern nach Trichomen. Ein Taschenmikroskop ist dein bestes Werkzeug.',
          params: [
            ['🔬', 'Werkzeug', 'Mikroskop 60x–100x'],
            ['🎯', 'Wo schauen', 'Blüten, nicht Blätter'],
            ['🚿', 'Spülen', '7–14 Tage vorher'],
            ['⏱️', 'Kontrolle', 'Alle 1–2 Tage']
          ],
          trichomes: [
            ['clear', 'Klar', 'Unreif: geringe Potenz. Noch nicht so weit.'],
            ['milky', 'Milchig', 'THC-Höhepunkt: zerebralste und stärkste Wirkung.'],
            ['amber', 'Bernstein', 'Körperliche, sedierende Wirkung: THC beginnt abzubauen.']
          ],
          steps: [
            'Die Trichome auf den <strong>Blüten</strong> (nicht auf den Zuckerblättern, die früher reifen) unter dem Mikroskop prüfen.',
            '<strong>Überwiegend milchig mit 10–20 % Bernstein</strong> = klassische Balance zwischen Potenz und Körperwirkung.',
            'Für eine entspanntere, sedierende Wirkung auf <strong>30 % Bernstein oder mehr</strong> warten.',
            'Braune Blütenstempel sind nur ein grober Hinweis: <strong>Trichome</strong> sind der zuverlässige Indikator.'
          ],
          tip: 'Eile in der letzten Woche kostet Potenz, Geschmack und Gewicht. Immer mit der Lupe bestätigen.'
        },
        {
          short: 'Trocknen & Curing',
          title: 'Trocknung & Curing',
          duration: '10–14 Tage + 2–8 Wochen',
          summary: 'Der Schritt, der eine ordentliche Blüte von einer exzellenten unterscheidet: Geschmack, Aroma und Milde.',
          params: [
            ['🌑', 'Umgebung', 'Völlige Dunkelheit'],
            ['🌡️', 'Temperatur', '18–20 °C'],
            ['💧', 'Luftfeuchtigkeit', '50–55 % rLF'],
            ['🫙', 'Curing', 'Luftdichte Gläser']
          ],
          steps: [
            'Die Zweige kopfüber in einem <strong>dunklen</strong> Raum mit sanfter, indirekter Luftbewegung aufhängen (nie einen Ventilator direkt auf die Blüten richten).',
            '<strong>18–20 °C und 50–55 % rLF für 10–14 Tage</strong> halten. Langsames Trocknen bewahrt die Terpene.',
            'Fertig ist es, wenn kleine Stiele knacken statt sich zu biegen.',
            'Maniküren und die Blüten in <strong>luftdichten Gläsern</strong> lagern, zu 70–75 % gefüllt.',
            '<strong>Gläser täglich lüften</strong> (10–15 min) in den ersten 2 Wochen; danach einmal pro Woche.'
          ],
          tip: 'Riecht das Glas beim Öffnen nach Ammoniak, ist die Blüte zu feucht: einige Stunden auslüften lassen, bevor du es wieder verschließt.'
        }
      ],
      errors: {
        title: '⚠️ 3 klassische Anfängerfehler, die du vermeiden solltest',
        items: [
          ['💦', 'Staunässe durch zu viel Gießen', '„Sicherheitshalber“ gießen ertränkt die Wurzeln: Ohne Sauerstoff faulen sie und die Pflanze hängt, obwohl sie genug Wasser hat.', 'nach Topfgewicht gießen und für gute Drainage sorgen.'],
          ['🧪', 'Zu frühe Überdüngung', 'Sämlinge brauchen keinen Dünger. Zu frühes Düngen verbrennt Spitzen und Wurzeln und blockiert Nährstoffe.', 'in der Wachstumsphase mit 1/4 der Dosis beginnen und langsam steigern.'],
          ['⏳', 'Überstürzte Ernte', 'Mit klaren Trichomen zu ernten bedeutet weniger Potenz, schlechteren Geschmack und weniger Ertrag.', 'Lupe benutzen und warten, bis die meisten Trichome milchig sind.']
        ]
      },
      footer: {
        disclaimer: 'Informationsinhalt für Erwachsene (18+). Informiere dich über die in deinem Land geltenden Gesetze zum Eigenanbau und halte sie ein.',
        back: 'Zurück zum Katalog'
      }
    },

    /* ============================== ITALIANO ============================== */
    it: {
      meta: {
        title: 'Guida alla Coltivazione in 5 Fasi • CannaCulture',
        description: 'Guida interattiva alla coltivazione: germinazione, vegetativa, fioritura, raccolta tramite tricomi, essiccazione e concia.'
      },
      nav: { catalog: 'Catalogo', guide: 'Guida alla Coltivazione', dispensary: 'Dispensario CSC' },
      hero: {
        eyebrow: 'Guida pratica · 5 fasi',
        title: 'Guida alla Coltivazione',
        subtitle: 'Dal seme al barattolo: tutto il ciclo spiegato passo dopo passo, con i parametri che contano davvero.'
      },
      ui: {
        prev: 'Indietro', next: 'Avanti', stage: 'Fase', of: 'di',
        params: 'Parametri chiave', steps: 'Passo dopo passo', tip: '💡 Consiglio chiave',
        trichomes: 'Lettura dei tricomi', fix: 'Soluzione:'
      },
      stages: [
        {
          short: 'Germinazione',
          title: 'Germinazione & Piantina',
          duration: '3–10 giorni + 2 settimane',
          summary: 'Il seme si risveglia. Umidità costante, buio e tanta delicatezza: è la fase più fragile del ciclo.',
          params: [
            ['🌡️', 'Temperatura', '22–25 °C'],
            ['💧', 'Umidità', '70–80 % UR'],
            ['🧪', 'pH dell’acqua', '6.0 – 6.5'],
            ['🌑', 'Luce', 'Buio → luce soffusa']
          ],
          steps: [
            'Metti i semi tra due <strong>tovaglioli di carta umidi</strong> (non zuppi) in un piatto coperto, in un luogo <strong>buio e tiepido</strong>.',
            'Controlla ogni 12 h: quando la radice principale (radichetta) spunta di <strong>0,5–1 cm</strong>, è il momento di trapiantare.',
            'Trapianta con cura in un substrato leggero tipo <strong>Light Mix</strong>, radice verso il basso a 0,5–1 cm di profondità, senza toccare la radichetta.',
            '<strong>Prime annaffiature minime:</strong> nebulizza o annaffia un piccolo cerchio attorno al fusto. Le radici giovani hanno bisogno di ossigeno, non di una pozzanghera.',
            'Usa acqua a <strong>pH 6.0–6.5</strong> e senza fertilizzanti: il Light Mix fornisce tutto il necessario nelle prime settimane.'
          ],
          tip: 'Meno è meglio: l’eccesso d’acqua è la prima causa di morte delle piantine (damping-off).'
        },
        {
          short: 'Vegetativa',
          title: 'Crescita Vegetativa',
          duration: '3–8 settimane',
          summary: 'La pianta costruisce la sua struttura: radici, fusti e foglie. Qui si definisce il potenziale del raccolto.',
          params: [
            ['💡', 'Fotoperiodo', '18 h luce / 6 h buio'],
            ['🌡️', 'Temperatura', '22–28 °C'],
            ['💧', 'Umidità', '55–70 % UR'],
            ['⚗️', 'Nutrizione', 'Azoto (N) leggero']
          ],
          steps: [
            'Mantieni un fotoperiodo <strong>18/6</strong> (18 h di luce e 6 h di buio) perché la pianta resti in fase vegetativa.',
            '<strong>Regola d’oro dell’irrigazione:</strong> solleva il vaso. Annaffia solo quando è chiaramente leggero; il ciclo umido-secco <strong>ossigena le radici</strong> e le stimola a crescere.',
            'Annaffia fino a ottenere un 10–20 % di drenaggio e lascia asciugare il substrato prima dell’irrigazione successiva.',
            'Introduci un fertilizzante per la crescita con un <strong>apporto leggero di azoto</strong>, partendo da 1/4–1/2 della dose del produttore.',
            'Trapianta in un vaso più grande quando le radici occupano il contenitore e mantieni una ventilazione costante per rinforzare i fusti.'
          ],
          tip: 'Foglie verde intenso e sane = azoto corretto. Punte bruciate = stai esagerando: riduci la dose.'
        },
        {
          short: 'Fioritura',
          title: 'Fioritura',
          duration: '8–10 settimane',
          summary: 'La pianta smette di allungarsi e concentra tutta la sua energia nel produrre fiori densi e resinosi.',
          params: [
            ['💡', 'Fotoperiodo', '12 h luce / 12 h buio'],
            ['🌡️', 'Temperatura', '20–26 °C'],
            ['💧', 'Umidità', '40–50 % UR'],
            ['⚗️', 'Nutrizione', 'Fosforo (P) + Potassio (K)']
          ],
          steps: [
            'Nelle varietà <strong>fotoperiodiche</strong>, passa a <strong>12/12</strong> per indurre la fioritura. Le autofiorenti fioriscono da sole senza cambiare il fotoperiodo.',
            'Rispetta il <strong>buio totale</strong>: qualsiasi infiltrazione di luce durante le 12 h notturne stressa la pianta e può causare ermafroditismo.',
            'Abbassa gradualmente l’umidità al <strong>40–50 % UR</strong> per evitare <strong>botrite</strong> (muffa delle cime) e <strong>oidio</strong>.',
            'Passa a un fertilizzante da fioritura ricco di <strong>fosforo e potassio</strong> e riduci l’azoto.',
            'Assicura una buona circolazione d’aria tra le cime e controlla ogni giorno l’interno dei fiori più densi.'
          ],
          tip: 'Nelle prime 2–3 settimane la pianta può raddoppiare la sua altezza (stretch): lascia spazio sufficiente sotto la luce.'
        },
        {
          short: 'Raccolta',
          title: 'Momento Ottimale di Raccolta',
          duration: 'Finestra di 1–2 settimane',
          summary: 'Non raccogliere a calendario: raccogli guardando i tricomi. Un microscopio tascabile è il tuo miglior strumento.',
          params: [
            ['🔬', 'Strumento', 'Microscopio 60x–100x'],
            ['🎯', 'Dove guardare', 'Cime, non foglie'],
            ['🚿', 'Lavaggio radici', '7–14 giorni prima'],
            ['⏱️', 'Controllo', 'Ogni 1–2 giorni']
          ],
          trichomes: [
            ['clear', 'Trasparenti', 'Immaturo: potenza bassa. Non è ancora il momento.'],
            ['milky', 'Lattiginosi', 'Picco di THC: effetto più cerebrale e potente.'],
            ['amber', 'Ambrati', 'Effetto corporeo e sedativo: il THC inizia a degradarsi.']
          ],
          steps: [
            'Osserva i tricomi sui <strong>fiori</strong> (non sulle foglioline zuccherine, che maturano prima) al microscopio.',
            '<strong>Maggioranza lattiginosi con 10–20 % ambrati</strong> = il classico equilibrio tra potenza ed effetto corporeo.',
            'Se cerchi un effetto più rilassante e sedativo, aspetta il <strong>30 % o più di ambrati</strong>.',
            'I pistilli marroni sono solo indicativi: i <strong>tricomi</strong> sono l’indicatore affidabile.'
          ],
          tip: 'La fretta nell’ultima settimana costa potenza, sapore e peso. Conferma sempre con la lente.'
        },
        {
          short: 'Essiccazione & Concia',
          title: 'Essiccazione & Concia',
          duration: '10–14 giorni + 2–8 settimane',
          summary: 'Il passaggio che distingue un fiore discreto da uno eccellente: sapore, aroma e morbidezza.',
          params: [
            ['🌑', 'Ambiente', 'Buio totale'],
            ['🌡️', 'Temperatura', '18–20 °C'],
            ['💧', 'Umidità', '50–55 % UR'],
            ['🫙', 'Concia', 'Barattoli ermetici']
          ],
          steps: [
            'Appendi i rami a testa in giù in uno spazio <strong>buio</strong>, con ventilazione leggera e indiretta (mai un ventilatore puntato sui fiori).',
            'Mantieni <strong>18–20 °C e 50–55 % UR per 10–14 giorni</strong>. Un’essiccazione lenta preserva i terpeni.',
            'È pronto quando i rametti piccoli si spezzano con uno schiocco invece di piegarsi.',
            'Manicura e conserva i fiori in <strong>barattoli di vetro ermetici</strong>, riempiti al 70–75 %.',
            '<strong>Arieggia i barattoli ogni giorno</strong> (10–15 min) per le prime 2 settimane; poi una volta a settimana.'
          ],
          tip: 'Se aprendo il barattolo senti odore di ammoniaca, il fiore è troppo umido: lascialo arieggiare qualche ora prima di richiuderlo.'
        }
      ],
      errors: {
        title: '⚠️ 3 Errori Classici da Principiante da Evitare',
        items: [
          ['💦', 'Ristagno per eccesso d’acqua', 'Annaffiare “per sicurezza” soffoca le radici: senza ossigeno marciscono e la pianta appare afflosciata pur avendo acqua in abbondanza.', 'annaffia in base al peso del vaso e garantisci un buon drenaggio.'],
          ['🧪', 'Sovrafertilizzazione precoce', 'Le piantine non hanno bisogno di concime. Fertilizzare troppo presto brucia punte e radici e blocca i nutrienti.', 'inizia in vegetativa con 1/4 della dose e aumenta gradualmente.'],
          ['⏳', 'Raccogliere di fretta', 'Tagliare con tricomi trasparenti significa meno potenza, sapore peggiore e meno peso finale.', 'usa la lente e aspetta che la maggior parte dei tricomi sia lattiginosa.']
        ]
      },
      footer: {
        disclaimer: 'Contenuto divulgativo per persone adulte (18+). Informati e rispetta la legislazione vigente nel tuo paese sull’autocoltivazione.',
        back: 'Torna al Catalogo'
      }
    }
  };

  /* ============================== ESTADO ============================== */
  const state = {
    lang: (function () {
      try {
        const saved = localStorage.getItem('kiosk_lang');
        if (SUPPORTED.includes(saved)) return saved;
      } catch (e) { /* localStorage no disponible */ }
      return 'es';
    })(),
    stage: (function () {
      const m = /^#etapa-([1-5])$/.exec(window.location.hash);
      return m ? Number(m[1]) - 1 : 0;
    })()
  };

  const $ = (sel) => document.querySelector(sel);

  function getPath(obj, path) {
    return path.split('.').reduce((o, k) => (o ? o[k] : undefined), obj);
  }

  /* ============================== RENDER ============================== */
  function renderStatic() {
    const t = I18N[state.lang];
    document.documentElement.lang = state.lang;
    document.title = t.meta.title;
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) metaDesc.setAttribute('content', t.meta.description);

    document.querySelectorAll('[data-i18n]').forEach((el) => {
      const value = getPath(t, el.getAttribute('data-i18n'));
      if (typeof value === 'string') el.textContent = value;
    });

    document.querySelectorAll('.lang-pill-btn').forEach((btn) => {
      const isActive = btn.dataset.lang === state.lang;
      btn.classList.toggle('active', isActive);
      btn.setAttribute('aria-pressed', String(isActive));
    });
  }

  function renderTabs() {
    const t = I18N[state.lang];
    const tabs = $('#stage-tabs');
    tabs.innerHTML = t.stages.map((s, i) => `
      <button type="button" role="tab" class="gc-step${i === state.stage ? ' active' : ''}${i < state.stage ? ' done' : ''}"
        id="stage-tab-${i + 1}" aria-controls="stage-panel" aria-selected="${i === state.stage}"
        tabindex="${i === state.stage ? 0 : -1}" data-stage="${i}">
        <span class="gc-step-node" aria-hidden="true">${STAGE_ICONS[i]}</span>
        <span class="gc-step-label"><span class="gc-step-num">${t.ui.stage} ${i + 1}</span>${s.short}</span>
      </button>`).join('');

    $('#stepper-fill').style.width = `${(state.stage / (t.stages.length - 1)) * 100}%`;
    $('#stage-panel').setAttribute('aria-labelledby', `stage-tab-${state.stage + 1}`);
  }

  function renderPanel(animate) {
    const t = I18N[state.lang];
    const s = t.stages[state.stage];

    const params = s.params.map(([icon, label, value]) => `
      <div class="gc-param">
        <span class="gc-param-icon" aria-hidden="true">${icon}</span>
        <span><span class="gc-param-label">${label}</span><span class="gc-param-value">${value}</span></span>
      </div>`).join('');

    const trichomes = s.trichomes ? `
      <h3 class="gc-section-label">${t.ui.trichomes}</h3>
      <div class="gc-trichomes">
        ${s.trichomes.map(([cls, name, desc]) => `
          <div class="gc-trichome ${cls}">
            <div class="gc-trichome-orb" aria-hidden="true"></div>
            <span class="gc-trichome-name">${name}</span>
            <span class="gc-trichome-desc">${desc}</span>
          </div>`).join('')}
      </div>` : '';

    const html = `
      <div class="gc-panel-inner${animate ? '' : ' no-anim'}">
        <header class="gc-panel-head">
          <div class="gc-panel-icon" aria-hidden="true">${STAGE_ICONS[state.stage]}</div>
          <div class="gc-panel-titles">
            <span class="gc-panel-tag">${t.ui.stage} ${state.stage + 1}</span>
            <h2 class="gc-panel-title">${s.title}</h2>
            <p class="gc-panel-summary">${s.summary}</p>
          </div>
          <span class="gc-duration">⏳ ${s.duration}</span>
        </header>

        <h3 class="gc-section-label">${t.ui.params}</h3>
        <div class="gc-params">${params}</div>

        ${trichomes}

        <div class="gc-body">
          <div>
            <h3 class="gc-section-label">${t.ui.steps}</h3>
            <ol class="gc-steps">${s.steps.map((step) => `<li>${step}</li>`).join('')}</ol>
          </div>
          <aside class="gc-side">
            <div class="gc-tip">
              <span class="gc-tip-label">${t.ui.tip}</span>
              <p>${s.tip}</p>
            </div>
          </aside>
        </div>
      </div>`;

    const panel = $('#stage-panel');
    panel.innerHTML = html;
    if (!animate) {
      const inner = panel.querySelector('.gc-panel-inner');
      if (inner) inner.style.animation = 'none';
    }

    $('#btn-stage-prev').disabled = state.stage === 0;
    $('#btn-stage-next').disabled = state.stage === t.stages.length - 1;
    $('#stage-counter').textContent = `${t.ui.stage} ${state.stage + 1} ${t.ui.of} ${t.stages.length}`;
  }

  function renderErrors() {
    const t = I18N[state.lang];
    $('#errors-grid').innerHTML = t.errors.items.map(([icon, title, text, fix], i) => `
      <article class="gc-error-card" id="error-card-${i + 1}">
        <div class="gc-error-head">
          <span class="gc-error-num" aria-hidden="true">${icon}</span>
          <h3 class="gc-error-title">${i + 1}. ${title}</h3>
        </div>
        <p class="gc-error-text">${text}</p>
        <p class="gc-error-fix"><strong>✅ ${t.ui.fix}</strong> ${fix}</p>
      </article>`).join('');
  }

  function renderAll(animate) {
    renderStatic();
    renderTabs();
    renderPanel(animate);
    renderErrors();
  }

  /* ============================== ACCIONES ============================== */
  function goToStage(index, focusTab) {
    const total = I18N[state.lang].stages.length;
    const next = Math.max(0, Math.min(total - 1, index));
    if (next === state.stage) return;
    state.stage = next;
    renderTabs();
    renderPanel(true);
    if (history.replaceState) history.replaceState(null, '', `#etapa-${next + 1}`);
    if (focusTab) {
      const tab = document.getElementById(`stage-tab-${next + 1}`);
      if (tab) tab.focus();
    }
  }

  function setLang(lang) {
    if (!SUPPORTED.includes(lang) || lang === state.lang) return;
    state.lang = lang;
    try { localStorage.setItem('kiosk_lang', lang); } catch (e) { /* noop */ }
    renderAll(false);
  }

  function bindEvents() {
    document.querySelectorAll('.lang-pill-btn').forEach((btn) => {
      btn.addEventListener('click', () => setLang(btn.dataset.lang));
    });

    const tabs = $('#stage-tabs');
    tabs.addEventListener('click', (e) => {
      const btn = e.target.closest('.gc-step');
      if (btn) goToStage(Number(btn.dataset.stage), false);
    });
    tabs.addEventListener('keydown', (e) => {
      const keys = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 };
      if (e.key in keys) {
        e.preventDefault();
        goToStage(state.stage + keys[e.key], true);
      } else if (e.key === 'Home') {
        e.preventDefault();
        goToStage(0, true);
      } else if (e.key === 'End') {
        e.preventDefault();
        goToStage(I18N[state.lang].stages.length - 1, true);
      }
    });

    $('#btn-stage-prev').addEventListener('click', () => goToStage(state.stage - 1, false));
    $('#btn-stage-next').addEventListener('click', () => goToStage(state.stage + 1, false));

    window.addEventListener('hashchange', () => {
      const m = /^#etapa-([1-5])$/.exec(window.location.hash);
      if (m) goToStage(Number(m[1]) - 1, false);
    });
  }

  function init() {
    renderAll(true);
    bindEvents();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Exposición mínima para depuración / integración futura
  window.CannaGrowGuide = { setLang, goToStage, I18N };
})();
