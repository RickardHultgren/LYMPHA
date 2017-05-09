---
layout: post
title: Sudden brain symptoms
---
How can a regular smartphone discover suddenly debuted symptoms related to the brain? I can imagine the following ways that a smartphone can help verify brain symptoms:

- Ask the patient questions about symptoms. E.g. headache, vomiting, difficult to swallow, etc.
- Investigate double vision. To do this, the patient can answer a question about pictures that are displayed on the screen. The camera on the display side can also be used to determine if any eye is dominant. The examination can be filmed and sent to the healthcare provider.

Listed below are the causes of acute-debuted brain symptoms and a flow-chart sketch describing the treatment:

- Bleeding
- Restriction in blood supply (ischemia) of certain parts of the brain; When blood does not reach all parts of the brain, symptoms arise from parts that do not have enough blood supply (ischemia). Symptoms that represent a part of the brain are called focal symptoms. An inadequate blood flow can be caused by an artery being either blocked (embolism) or broken (bleeding). In the case of persistent symptoms after 24 hours, the condition is called *stroke*. If the blood passes the blockade within 24 hours the condition is called TIA. The essence of TIA is that the risk of stroke is about 10% within seven days since more blood clots (also called embolics) can loosen from vessels with severe arteriosclerosis. These embolics travel on to the brain and also to the eye that is supplied by the same arteries as some parts of the brain. Therefore, ischemia in the eye (amarosis fugax) also increases the risk of later stroke. So the definition of a TIA is, therefore, amarosis fugax or focal neurological symptoms disappearing within 24 hours.
<p class="dragscroll" style="border:0.2em solid #aaaaaa;">
![<img src="http://rickardhultgren.github.io/lympha/images/brain1.jpg">](http://rickardhultgren.github.io/lympha/images/brain1.jpg) 
</p>
LYMPHA-script:
<pre class="dragscroll">

intracranial_hemorrhage -> headache_thunderclap_in_Subarachnoidal_bleeding ;
intracranial_hemorrhage -> vomiting ;
intracranial_hemorrhage -> decreased_consciousness ;
intracranial_hemorrhage -> hypertension ;

cardiac_embolism -> embolus_vertebral ;
macrovascular_disease -> embolus_vertebral ;
lacunar_infarction -> embolus_vertebral ;

cardiac_embolism -> embolus_carotis ;
macrovascular_disease -> embolus_carotis ;
lacunar_infarction -> embolus_carotis ;

palsy -> acute_CT_skull ;
aphasia -> acute_CT_skull ;
amaurosis_fugax -> acute_CT_skull ;

embolus_carotis -> palsy ;
embolus_carotis -> numbness ;
embolus_carotis -> aphasia ;
embolus_carotis -> amaurosis_fugax ;

cerebellar_haemorrhage -> balance_defect ;

visual_field_defect -> acute_CT_skull ;
balance_defect -> acute_CT_skull ;
vertigo -> acute_CT_skull ;
dysarthria -> acute_CT_skull ;

embolus_vertebral -> visual_field_defect ;
embolus_vertebral -> balance_defect ;
embolus_vertebral -> vertigo ;
embolus_vertebral -> diplopia ;
embolus_vertebral -> dysarthria ;

Lateral_medullary_syndrome -> dysphagia ;
Lateral_medullary_syndrome -> slurred_speech ;
Lateral_medullary_syndrome -> ataxia ;
Lateral_medullary_syndrome -> facial_pain ;
Lateral_medullary_syndrome -> vertigo ;
Lateral_medullary_syndrome -> nystagmus ;
Lateral_medullary_syndrome -> Horners_syndrome ;
Lateral_medullary_syndrome -> diplopia ;

Intracerebral_haemorrhage -> increased_ICP;

increased_ICP -> headache_thunderclap_in_Subarachnoidal_bleeding ;
increased_ICP -> decreased_consciousness ;
increased_ICP -> lethargy ;
increased_ICP -> weakness ;
increased_ICP -> numbness ;
increased_ICP -> diplopia ;
increased_ICP -> seizures ;
increased_ICP -> vomiting ;

headache_thunderclap_in_Subarachnoidal_bleeding -> acute_CT_skull ;
decreased_consciousness -> acute_CT_skull ;
hypertension -> acute_CT_skull ;
lethargy -> acute_CT_skull ;
weakness -> acute_CT_skull ;
numbness -> acute_CT_skull ;
diplopia -> acute_CT_skull ;
seizures -> acute_CT_skull ;
vomiting -> acute_CT_skull ;
confusion -> acute_CT_skull ;
neck_stiffness -> acute_CT_skull ;
decreased_consciousness -> acute_CT_skull ;

dysphagia -> acute_CT_skull ;
slurred_speech -> acute_CT_skull ;
ataxia -> acute_CT_skull ;
facial_pain -> acute_CT_skull ;
nystagmus -> acute_CT_skull ;
Horners_syndrome -> acute_CT_skull ;

cerebral_aneurysm -> Subarachnoidal_bleeding ;
trauma -> Subarachnoidal_bleeding ;

Subarachnoidal_bleeding -> headache_thunderclap_in_Subarachnoidal_bleeding ;
Subarachnoidal_bleeding -> confusion ;
Subarachnoidal_bleeding -> seizures ;
Subarachnoidal_bleeding -> vomiting ;
Subarachnoidal_bleeding -> neck_stiffness ;
Subarachnoidal_bleeding -> decreased_consciousness ;

acute_CT_skull  -> IF_NO_bleeding ;
IF_NO_bleeding -> thrombolsysis_within_4_5h_hours_after_debute_ASA300TO320mg_OR_Clopidogrel75mg ;
thrombolsysis_within_4_5h_hours_after_debute_ASA300TO320mg_OR_Clopidogrel75mg -> ECG ;
ECG -> carotid_duplex ;
carotid_duplex -> heart_Eco ;
heart_Eco -> MR;

acute_CT_skull  -> IF_subarachnoid_bleeding ;
IF_subarachnoid_bleeding -> angiography ;

acute_CT_skull  -> IF_MAYBE_bleeding ;
IF_MAYBE_bleeding -> LP_after_12h ;
LP_after_12h -> Xanthochromia_OR_high_bilirubin ;
Xanthochromia_OR_high_bilirubin -> angiography ;
angiography -> endovascular_coiling_OR_open_clip ;
endovascular_coiling_OR_open_clip -> tablet_Nimotop2_TO_3_weeks_to_prevent_vasospasm ;
tablet_Nimotop2_TO_3_weeks_to_prevent_vasospasm -> Rehabilitation ;
tablet_Nimotop2_TO_3_weeks_to_prevent_vasospasm -> hydrocephalus_control ;
tablet_Nimotop2_TO_3_weeks_to_prevent_vasospasm -> vitreous_detachment_control ;

acute_CT_skull  -> IF_intracranial_hemorrhage ;
IF_intracranial_hemorrhage -> IF_waran_OR_thrombolysis_treatment ;
IF_waran_OR_thrombolysis_treatment -> correction_of_PK_INR ;
IF_intracranial_hemorrhage -> correction_of_blood_pressure ;
IF_intracranial_hemorrhage -> correction_of_ICP_with_mannitol ;

</pre>
