---
layout: post
title: headaches
---

Usually a headache passes by itself, but when does a patient need help with that kind of problem? I can see two reasons:
- *Primarly headache*; The patient cannot manage the pain itself.
- *Secundary headache*; There are signs that can indicate a serious underlying cause that the patient cannot manage on her own. In the events of following situation you can suspect an underlying cause:
   - After a blow to the head gets headache and becomes dizzy.
   - A headache that gradually increases over a few days.
   - A headache that is correlated with pain around one eye and vision change.
   - Headache and pain in the temple, chewing pain, fatigue or light fever.
   - Sudden severe headache.
   - A headache while having a fever and being stiff in the neck.

In all cases of secundary headache ununsual symptoms or and event is correlated to the headache. The patient goes to the physician when those unusual things uccors. The unusual circumstances should indicate more advanced examinations like:

*Headache examintion:*
- eye fundus examination
- body temperture
- neurological examination
- Blood tests in questions are
   - Complete blood count
   - electrolytes and creatinine
   - CRP
   - ESR
   - P-­Glucose

This should in most cases be followed by imaging diagnostics (CT or MR). I think it could be rather hard to make the process of further diagnostics more effective when it comes to severe underlying causes. Nevertheless a visual presentation of the proceeding can often be valuable for the patient. 


When there is no symptoms and findings that can be correlated to severe underlying causes, then the issue is a primar headache. This group of pahthologies are caused by disturbances in either the nervfibers or other parts of the nervous system that are connected to pain. Here are the most important pathological entities:
- Tension Headaches
- Migraine
- Idiopathic trigeminus neuralgia
- Horton's headache/cluster headache

The treatment of all types of primary headache follows this algorithm:


Pseudocode:
<pre class="dragscroll">
IF primary_headache_attack THEN primary_headache_attack_treatment
ELSE primary_headache_preventiv_treatment
</pre>

...or to put it in the language of <span class="sc">lympha</span>:
<pre class="dragscroll">
primary_headache_attack? == 1 -> primary_headache_attack_treatment ;
primary_headache_attack? == 0 -> primary_headache_preventiv_treatment ;
</pre>

An "headache attack button" on your smartphone could work as a treatment appraisal. Not only the occurrence of attacks can be measured, but also the duration time and optionally the intensity. Depending on the evolution of symptoms the program can recommend different medications in line with medical protocols. The program flow would look something like below:
<pre class="dragscroll">
IF headache attack THEN ask for secondary headache symptoms
   IF secondary headache symptoms THEN recommend getting in touch with health care
   ELSE
</pre>


I think there is a big need of communication about the attacks.   The problem with attacks is that it disabilitate you from doing what you planned to do. Often that means that you have to put extra effort in announcing your situation. This effort costs energy that you don't have, since you must focus on your attack. It would be much easier to just put a "attack-button" on you cellphone instead of starting a viscious cycle. 

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




