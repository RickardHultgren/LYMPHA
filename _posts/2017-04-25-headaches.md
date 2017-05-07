---
layout: post
title: headaches
---

Usually a headache passes by itself, but when does a patient need help with that kind of problem? I can see two reasons:
- The patient cannot manage the pain itself.
- There are signs that can indicate a serious underlying cause that the patient cannot manage on her own. In the events of following situation you can suspect an underlying cause:
   - After a blow to the head gets headache and becomes dizzy.
   - A headache that gradually increases over a few days.
   - A headache that is correlated with pain around one eye and vision change.
   - Headache and pain in the temple, chewing pain, fatigue or light fever.
   - Sudden severe headache.
   - A headache while having a fever and being stiff in the neck.



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

Bellow is a flow-chart and <span class="sc">lympha</span>-script describing symptoms associated with underlying causes of headache.

<p class="dragscroll" style="border:0.2em solid #aaaaaa;">
![<img src="http:
//rickardhultgren.github.io/lympha/images/headache.jpg">](http://rickardhultgren.github.io/lympha/images/headache.jpg)
</p>
LYMPHA-script:



<pre class="dragscroll">

intracranial_expansiveness -> epileptic_seizure ;
intracranial_expansiveness -> Papilledema ;
intracranial_expansiveness -> neurological_deficits ;
intracranial_expansiveness -> personality_change ;
intracranial_expansiveness -> headache_AND_vomiting ;
intracranial_expansiveness -> headache_increasing_when_exertion ;
vessel_malformation -> intracranial_expansiveness ;
intracranial_expansiveness -> never_changing_side_AND_atypical_aura ;
intracranial_expansiveness -> pupill_dillatation ;
intracranial_expansiveness -> unconscious_OR_confusion ;

epileptic_seizure -> CT_head ;
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

face_pain_OR_small_pupil_OR_hanging_eyelid -> MR_brain ;
expanding_aneurysm -> diplopia ;
diplopia -> MR_brain ;
aneurysm -> headache_increasing_when_exertion ;
headache_increasing_when_exertion -> MR_brain ;
ache_in_the_back_of_head -> MR_brain ; 
endocrine_dysfunction -> MR_brain ;
MR_brain -> IF_pathology_in_skull_base ;

meningitis -> neck_stiffness ;
meningitis -> fever ;
meningitis -> unconscious_OR_confusion ;
neck_stiffness -> blood_AND_test_body_temperature ;
fever -> blood_AND_test_body_temperature ;
unconscious_OR_confusion -> blood_AND_test_body_temperature ;
CT_head  -> IF_MAYBE_high_ICP ;
IF_MAYBE_high_ICP -> LP ;
Giant_cell_arteritis -> headache_patient_50y_older ;
headache_patient_50y_older -> blood_AND_test_body_temperature ;

</pre>




