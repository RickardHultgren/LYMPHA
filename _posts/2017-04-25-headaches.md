---
layout: post
title: Taking leadership over the headache
---

Headache
Usually a headache passes by itself. So when should a patient go to the doctor? I can see two reasons why a patient should meet a physician:
- The patient cannot manage the pain.
- There are sings that can indicate a serious underlying cause that the patient cannot manage on her own.
In both cases the patient has a problem with management. Would it not be logical if the phsycian could manage the problem instead of the patient? That might sometime be the case, e.g. prescribing pills. No matter if the doctor manages or not, the physician always have to take responsebility  most often there is   The healthcare professional can solve the problem with an algorithmic approach.


The role of the pysician is to response to the management problem that the patient has. Sometimes the pysician also must be accountable for giving medicine or performing surgery. There are many reasons for headaches, and patients suffering from the same illness or injury can have different kind of headaches. The headache can be very changing even in one person. In other words, headache is a very non exact symptom. With proper examination a physician can diagnose the reason behind headaches. But in the majority of cases it is not necessary to go to the physician. 

Sök vård:
- efter ett slag mot huvudet får huvudvärk och blir slö
- har en huvudvärk som gradvis ökar under några dagar eller veckor
- får ont kring ena ögat och synförändring
- har ont vid tinningen, tuggsmärta, trötthet eller lätt feber
- plötsligt får svår huvudvärk
- har huvudvärk samtidigt som du har feber och är stel i nacken.




**När bör CT skalle utan/med kontrast aktualiseras?**
- Misstänk intrakraniell expansivitet vid:
- Epileptiskt anfall.
- Staspapill.
- Ökande neurologiska bortfallssymtom; motoriska, sensoriska, dubbelseende, synfältsstörningar eller kortvariga episoder med nedsatt syn.
- Personlighetsförändring, t.ex. ökande apati, aggressionsutbrott eller oklar ångest.
- Nytillkommen huvudvärk med kräkningar.
- Nytillkommen huvudvärk som ökar vid kroppsansträngning, hosta eller krystning.
- Migränliknande huvudvärk med atypisk aura, som aldrig skiftar sida (misstänk arteriovenös kärlmissbildning).
- Huvudvärksattack med dubbelseende eller ensidig pupillvidgning (misstänk aneurysm).
- Medvetandeförlust vid huvudvärk (misstänkt cysta eller tumör i anslutning till hjärnans ventrikelsystem).
- Misstänk sinustrombos eller intrakranieil hypertension vid:
- Nydebuterad huvudvärk, som inte viker inom cirka 3 dygn utan snarare ökar, oftast (men ej alltid) kombinerad med allmänpåverkan som illamående, synnedsättning eller neurologiska bortfallssymtom.
- Staspapill.
- Debut av ovanstående i anslutning till förlossning, p-piller eller annan medicinering.
- Misstänk subaraknoidalblödning vid:
- Urakut debuterande intensiv huvudvärk, ibland men ejalltid i anslutning till kroppsansträngning, hosta, krystning eller sexuell aktivitet.
- Samtidig nackstyvhet, ljuskänslighet och/eller illamående.

**När bör MR hjlima, eventuellt med MR-anglograñ, aktualiseras?**
Sjukdomar i hypofysområdet, skallbasen och bakre skallgropen visualiseras optimalt med MR, som i sådana fall kan övervägas som primär undersökning, alternativt som komplettering efter datortomografi.
- Akut ensidig ansiktssmärta med liten pupill och nedhängande ögonlock
- Huvudvärksattack med dubbelseende eller ensidig pupillvidgning (misstänk expanderande aneurysm).
- Tilltagande huvudvärk vid kroppsansträngning, hosta eller krystning (misstänk expanderande aneurysm eller process i bakre skallgrop). kvarstående misstanke om sinustrombos, med symtom enligt ovan. samma sida, debut av/risk för ischemisk stroke inom några dygn (misstänk karotisdissektion).
- Akut ensidig värk i bakhuvud; debut av/risk för ischemisk stroke inom några dygn (misstänk vertebralisdissektion).
- Tecken till endokrin dysfunktion, Lex. amenorré, akromegali, försenad Iängdtillväxt (misstänk hypofystumör).

När bör lumbalpunktlon övervägas?
- Vid samtidig feber, nackstyvhet, allmänpåverkan, förvirring (misstänk meningit, encefallt).
- Vid kvarstående misstanke om subaraknoidalblödning trots normal datortomografi skalle.
- Vid misstanke om intrakraniell hypertension trots normal datortomografi, med symtom enligt ovan.

När bör blodprovsutredning övervägas?
- Nydebuterad långdragen huvudvärk över 50 års ålder (misstänk temporalisarterit)

*Headache examintion:*
- eye fundus examination
- body temperture
- neurological examination

indications for CT:
-
-


-Akut DT-­‐hjärna om SAH-­‐misstanke
- För vidare SAH-­‐handläggning se sid.4
-Lab
- B-­‐stat
- El-­‐Krea
- CRP
- SR
- P-­‐Glc
- Temp
- U-­‐prov

neck-stiffness
- Papillödem!
- body temperture - fever
- Neurologi?
- Akut DT-­‐hjärna om SAH-­‐misstanke
- För vidare SAH-­‐handläggning se sid.4
- Lab
- B-­‐stat
- El-­‐Krea
- CRP
- SR
- P-­‐Glc
- Temp
- U-­‐prov







<p class="dragscroll" style="border:0.2em solid #aaaaaa;">
![<img src="http:
//rickardhultgren.github.io/lympha/images/aura.jpg">](http://rickardhultgren.github.io/lympha/images/aura.jpg)
</p>
LYMPHA-script:



<pre class="dragscroll">
cerebral_aneurysm -> Subarachnoidal_bleeding ;
Subarachnoidal_bleeding -> headache_thunderclap_in_Subarachnoidal_bleeding ;

at,El-­‐Krea, CRP, SR, P-­‐Glc, Temp, U-­‐prov

Subarachnoidal_bleeding -> confusion ;
Subarachnoidal_bleeding -> seizures ;
Subarachnoidal_bleeding -> vomiting ;
Subarachnoidal_bleeding -> neck_stiffness ;
Subarachnoidal_bleeding -> decreased_consciousness ;
acute_CT_skull -> IF_subarachnoid_bleeding ;
IF_subarachnoid_bleeding -> angiography ;
</pre>



