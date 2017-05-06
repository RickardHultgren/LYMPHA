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
 
Bellow is a flow-chart and <span class="sc">lympha</span>-script describing symptoms associated with underlying causes of headache.
 
*Headache examintion:*
- eye fundus examination
- body temperture
- neurological examination

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
//rickardhultgren.github.io/lympha/images/headache.jpg">](http://rickardhultgren.github.io/lympha/images/headache.jpg)
</p>
LYMPHA-script:



<pre class="dragscroll">

intracranial_expansiveness -> epileptic_seizure ;
intracranial_expansiveness -> Papilledema ;
intracranial_expansiveness -> neurological_deficits_Motor_ANDOR_sensory ;
intracranial_expansiveness -> personality_change ;
intracranial_expansiveness -> headache_AND_vomiting ;
intracranial_expansiveness -> headache_increasing_when_exertion ;
vessel_malformation -> intracranial_expansiveness ;
intracranial_expansiveness -> never_changing_side_AND_atypical_aura ;
intracranial_expansiveness -> pupill_dillatation ;
intracranial_expansiveness -> unconscious_OR_confusion ;

epileptic_seizure -> CT_head ;
Papilledema -> CT_head ;
neurological_deficits_Motor_ANDOR_sensory -> CT_head ;
headache_AND_vomiting -> CT_head ;
headache_increasing_when_exertion -> CT_head ;
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

facial_pain_AND_small_pupil_AND_hanging_eyelids -> MR_brain ;
expanding_aneurysm -> diplopia ;
diplopia -> MR_brain ;
aneurysm -> headache_increasing_when_exertion ;
headache_increasing_when_exertion -> MR_brain ;
Acute_unilateral_ache_in_the_back_of_head -> MR_brain ; 
Signs_of_endocrine_dysfunction -> MR_brain ;

meningitis -> neck_stiffness ;
meningitis -> fever ;
meningitis -> unconscious_OR_confusion ;
neck_stiffness -> blood_test ;
fever -> blood_test ;
unconscious_OR_confusion -> blood_test ;
CT_head  -> IF_MAYBE_high_ICP ;
IF_MAYBE_high_ICP -> LP ;

Giant_cell_arteritis -> headache_patient_50y_older ;
headache_patient_50y_older -> blood_test ;

</pre>




