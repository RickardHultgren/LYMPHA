---
layout: post
title: headaches
---

Usually a headache passes by itself, but when does a patient need help with that kind of problem? I can see two reasons:
- The patient cannot manage the pain itself.
- There are signs that can indicate a serious underlying cause that the patient cannot manage on her own. In the events of following situation you can suspect an underlying cause:
  - After a blow to the head gets headache and becomes sore.
  - A headache that gradually increases over a few days.
  - A headache that is correlated with pain around one eye and vision change.
  - Headache and pain in the temple, chewing pain, fatigue or light fever.
  - Sudden severe headache.
  - A headache while having a fever and being stiff in the neck.
 
 
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
intracranial_expansiveness -> Increasing_neurological_deficits_Motor_ANDOR_sensory ;
intracranial_expansiveness -> personality_change ;
intracranial_expansiveness -> headache_AND_vomiting ;
intracranial_expansiveness -> headache_increasing_when_exertion ;
vessel_malformation -> intracranial_expansiveness ;
intracranial_expansiveness -> Migraine_like_headache_atypical_aura_never_changing_side ;
intracranial_expansiveness -> Headache_attack_AND_pupill_dillatation ;
intracranial_expansiveness -> Loss_of_consciousness_in_headache ;

epileptic_seizure -> CT_head ;
Papilledema -> CT_head ;
Increasing_neurological_deficits_Motor_ANDOR_sensory -> CT_head ;
headache_AND_vomiting -> CT_head ;
headache_increasing_when_exertion -> CT_head ;
Migraine_like_headache_with_atypical_aura_never_changing_side -> CT_head ;
Headache_attack_AND_pupill_ dillatation -> CT_head ;
Loss_of_consciousness_in_headache -> CT_head ;

medications_like_eg_COCP -> sinus_thrombosis ;

sinus_thrombosis -> headache_not_weaken_within_3_days ;
sinus_thrombosis -> Papilledema ;

headache_not_weaken_within_3_days -> CT_head ;

cerebral_aneurysm -> Subarachnoidal_bleeding ;
Subarachnoidal_bleeding -> headache_thunderclap ;

Subarachnoidal_bleeding -> confusion ;
Subarachnoidal_bleeding -> seizures ;
Subarachnoidal_bleeding -> vomiting ;
Subarachnoidal_bleeding -> neck_stiffness ;
Subarachnoidal_bleeding -> decreased_consciousness ;

confusion -> CT_head ;
seizures -> CT_head ;
vomiting -> CT_head ;
neck_stiffness -> CT_head ;
decreased_consciousness -> CT_head ;
CT_head -> IF_subarachnoid_bleeding 
IF_subarachnoid_bleeding -> angiography ;

CT_head -> IF_MAYBE_bleeding ;
IF_MAYBE_bleeding -> LP_after_12h ;
LP_after_12h -> Xanthochromia_OR_high_bilirubin ;
Xanthochromia_OR_high_bilirubin -> angiography ;
angiography -> endovascular_coiling_OR_open_clip ;

facial_pain_AND_small_pupil_AND_hanging_eyelids -> MR_brain ;
expanding_aneurysm -> diplopia ;
expanding_aneurysm -> headache ;
headache -> MR_brain ;
diplopia -> MR_brain ;
aneurysm -> headache_increasing_when_exertion ;
headache_increasing_when_exertion -> MR_brain ;
Acute_unilateral_ache_in_the_back_of_head -> MR_brain ; 
Signs_of_endocrine_dysfunction_Amenorrhea_acromegaly_delayed_lung_growth  -> MR_brain ;

meningitis -> fever_AND_neck_stifness_AND_confusion ;
CT_head  -> IF_MAYBE_high_ICP ;
IF_MAYBE_high_ICP -> LP ;

Giant_cell_arteritis -> headache ;
headache -> blood_test ;

</pre>




