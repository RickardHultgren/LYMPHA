---
layout: post
title: headaches
---

**How can a smartphone be used in order to treat migraine?**

There exist already a lot of migraine diary apps. Usualy they such diaries are used in order to understand what triggers an attack. But a "headache attack button" could potentially also be used as a treatment appraisal in both migraine and tension headache. Not only the occurrence of attacks can be measured, but also the duration time and optionally the intensity. Accompanied symptoms can be noted. Depending on the evolution of symptoms the program can recommend different medications and doctor visits in line with medical protocols. I think there is also a big need of communication about the attacks. The problem with attacks is that it disabilitate you from doing what you planned to do. Often that means that you have to put extra effort in announcing your situation. This effort costs energy that you don't have, since you must focus on your attack. Instead of starting this viscious cycle it would be much easier if the "attack-button" on your smartphone could tell others about your condition. This could be done e.g. by automatic SMS-texting or starting scripts for rewritting calender files (.ics).

**Medical background**

Usually a headache passes by itself, but when does a patient need help with that kind of problem? I can see two reasons:
- *Primarly headache*; The patient cannot manage the pain itself.
- *Secundary headache*; There are signs that can indicate a serious underlying cause that the patient cannot manage on her own. In the events of following situation you can suspect an underlying cause:
   - After a blow to the head gets headache and becomes dizzy.
   - A headache that gradually increases over a few days.
   - A headache that is correlated with pain around one eye and vision change.
   - Headache and pain in the temple, chewing pain, fatigue or light fever.
   - Sudden severe headache.
   - A headache while having a fever and being stiff in the neck.

Secundary headache is often correlated to ununsual symptoms or and event is correlated to the headache. The patient goes to the physician when those unusual things uccors. The unusual circumstances should indicate more advanced examinations like:

*Headache examintion:*
- eye fundus examination
- body temperture
- neurological examination
- Blood tests in questions are
   - Complete blood count
   - electrolytes and creatinine
   - CRP
   - ESR
   - P-Glucose

This should in most cases be followed by imaging diagnostics (CT or MR). I think it could be rather hard to make the process of further diagnostics more effective when it comes to severe underlying causes. Nevertheless a visual presentation of the proceeding can often be valuable for the patient. 


When there is no symptoms and findings that can be correlated to severe underlying causes, then the issue is a primar headache. This group of pahthologies are caused by disturbances in either the nervfibers or other parts of the nervous system that are connected to pain. But other symptoms apart from the headache can also occur in primary headache. Sometimes it is exactly the same symptoms as in secundary headache. The difference between primary and secundary headache is in those cases the pattern of symptoms. A case where the pattern was overseen is presented in this <a href="http://www.aftonbladet.se/senastenytt/ttnyheter/inrikes/article24821315.ab">article written in Swedish</a>. The patient suffered three months from headaches with correlated nausea, vomiting and declining in body mass. During the period the patient met several GPs and got finally refered to a psychiatric unit (eh???) wherefrom she was referred to MR. The MR showed a brain tumor. The patient went through an acute surgery and died in a surgical wound infection. Perhaps the patient's life could have been saved if the tumor was found a couple of months earlier. So a good understanding of accompanied symptoms is crusial. Here are the most important pathological primary-headache entities with its accompanied symptoms:
- *Tension headaches*; Can be either episodic (hours to days) or chronic. The intensity varies often during an episode.
- *Migraine*; Occurs in distinct attacks that lasts from four hours to three days. The pain is often increasing during an attack. A visual phenomenen called aura can occur before the headache. Also paresthesias can occur before an attack. Accompanied symptoms can be vomiting, light and sound hypersensitivity. Frequency is about six per month to one per year. As opposed to this frequence, do growing tumors have a increasing frequency.
- *Idiopathic trigeminus neuralgia*; High intensity during seconds to up to two minutes, many times aday. Starts often after touching trigger points in face or mouth.
- *Horton's headache/cluster headache*; Intense attacks with a duration between 15 minutes and 3 hours. Frequency up to 8 aday often during a period of about a week per year. Accompanied symptoms in eyes and nose on one side. 

The treatments of all types of primary headache follow the principle that there is one regim for preventing an attack, and another regim should be appllied while having an attack.

Bellow is a flow-chart and <span class="sc">lympha</span>-script describing symptoms associated with underlying causes of headache.

<p class="dragscroll" style="border:0.2em solid #aaaaaa;">
![<img src="http:
//rickardhultgren.github.io/lympha/images/headache.jpg">](http://rickardhultgren.github.io/lympha/images/headache.jpg)
</p>
LYMPHA-script:



<pre class="dragscroll">

intracranial_expansiveness -> seizure ;
intracranial_expansiveness -> Papilledema ;
intracranial_expansiveness -> neurological_deficits ;
intracranial_expansiveness -> personality_change ;
intracranial_expansiveness -> headache_AND_vomiting ;
intracranial_expansiveness -> headache_increasing_when_exertion ;
vessel_malformation -> intracranial_expansiveness ;
intracranial_expansiveness -> never_changing_side_AND_atypical_aura ;
intracranial_expansiveness -> pupill_dillatation ;
intracranial_expansiveness -> unconscious_OR_confusion ;

seizure -> CT_head ;
Papilledema -> CT_head ;
neurological_deficits -> CT_head ;
headache_AND_vomiting -> CT_head ;
never_changing_side_AND_atypical_aura -> CT_head ;
pupill_dillatation -> CT_head ;
unconscious_OR_confusion -> CT_head ;

medications_like_eg_COCP -> sinus_thrombosis ;

sinus_thrombosis -> headache_not_weaken_within_3_days ;
sinus_thrombosis -> Papilledema ;

headache_not_weaken_within_3_days -> CT_head ;

cerebral_aneurysm -> Subarachnoidal_bleeding ;
Subarachnoidal_bleeding -> headache_thunderclap ;
headache_thunderclap -> CT_head ;

Subarachnoidal_bleeding -> seizures ;
Subarachnoidal_bleeding -> vomiting ;
Subarachnoidal_bleeding -> neck_stiffness ;
Subarachnoidal_bleeding -> unconscious_OR_confusion ;

seizures -> CT_head ;
vomiting -> CT_head ;
neck_stiffness -> CT_head ;
CT_head -> IF_subarachnoid_bleeding ;
IF_subarachnoid_bleeding -> angiography ;

CT_head -> IF_MAYBE_bleeding ;
IF_MAYBE_bleeding -> LP_after_12h ;
LP_after_12h -> Xanthochromia_OR_high_bilirubin ;
Xanthochromia_OR_high_bilirubin -> angiography ;
angiography -> endovascular_coiling_OR_open_clip ;

coritis_dissection -> face_pain_OR_small_pupil_OR_hanging_eyelid ;
face_pain_OR_small_pupil_OR_hanging_eyelid -> MR_brain ;
expanding_aneurysm -> diplopia ;
diplopia -> MR_brain ;
aneurysm -> headache_increasing_when_exertion ;
headache_increasing_when_exertion -> MR_brain ;
vertebralis_dissection -> ache_in_the_back_of_head ;
ache_in_the_back_of_head -> MR_brain ; 
endocrine_dysfunction -> MR_brain ;
MR_brain -> IF_pathology_in_skull_base ;

meningitis -> neck_stiffness ;
meningitis -> fever ;
meningitis -> unconscious_OR_confusion ;
neck_stiffness -> blood_AND_test_body_temperature ;
unconscious_OR_confusion -> blood_AND_test_body_temperature ;
CT_head  -> IF_MAYBE_high_ICP ;
IF_MAYBE_high_ICP -> LP ;

Giant_cell_arteritis -> bruits ;
Giant_cell_arteritis -> fever ;
Giant_cell_arteritis -> headache ;
Giant_cell_arteritis -> tenderness_and_sensitivity_on_the_scalp ;
Giant_cell_arteritis -> jaw_claudication ;
Giant_cell_arteritis -> tongue_claudication ;
Giant_cell_arteritis -> reduced_visual_acuity ;
Giant_cell_arteritis -> acute_visual_loss ;
Giant_cell_arteritis -> diplopia ;
Giant_cell_arteritis -> acute_tinnitus ;
Giant_cell_arteritis -> polymyalgia_rheumatica ;

bruits -> blood_AND_test_body_temperature ;
fever -> blood_AND_test_body_temperature ;
headache -> blood_AND_test_body_temperature ;
tenderness_and_sensitivity_on_the_scalp -> blood_AND_test_body_temperature ;
jaw_claudication -> blood_AND_test_body_temperature ;
tongue_claudication -> blood_AND_test_body_temperature ;
reduced_visual_acuity -> blood_AND_test_body_temperature ;
acute_visual_loss -> blood_AND_test_body_temperature ;
diplopia -> blood_AND_test_body_temperature ;
acute_tinnitus -> blood_AND_test_body_temperature ;
polymyalgia_rheumatica -> blood_AND_test_body_temperature ;

</pre>




