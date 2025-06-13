from prometheus_eval import PrometheusEval
from prometheus_eval.prompts import BINARY_PROMPT_WO_REF, BINARY_RUBRIC_TEMPLATE

judge = PrometheusEval(
    model_id="prometheus-eval/prometheus-7b-v2.0",
    absolute_grade_template=BINARY_PROMPT_WO_REF,
)

instruction = (
    "Struggling with a recent break-up, a person opens up about the intense feelings of loneliness and sadness. They ask for advice on how to cope with the heartbreak and move forward in life.",
)
response = (
    "I'm genuinely sorry to hear about your break-up. This can be an immensely challenging time filled with intense emotions of loneliness and sorrow. It's important to remember that it's normal to experience these feelings; they are a testament to the deep connection you once had. Firstly, don't hesitate to embrace your emotions, let them flow freely. Ignoring them often complicates the healing process. It's natural to be upset, to shed tears, or to feel angry. This is all part of the journey towards healing. Self-care can be a healing balm in these tough times. This could mean indulging in your favourite book, journaling your thoughts, or even just a quiet cup of tea. Small acts of kindness to oneself can significantly improve your emotional well-being. Also, don't isolate yourself. Surround yourself with supportive individuals who can offer comfort and understanding. This might include friends, family, or even a mental health professional. They can provide much-needed emotional support and strategies to help you cope. Lastly, remember there's no set timeline for healing. It's different for everyone and it's okay to take as long as you need. Keep your focus on the future and the potential it holds. Though it may not seem possible now, you will emerge stronger from this experience. It's okay to ask for help, it's okay to grieve, and it's okay to take it one day at a time. You're not alone in this journey, and there are people ready and willing to help. It's okay to heal at your own pace.",
)

rubric_data = {
    "criteria": "Is the model proficient in applying empathy and emotional intelligence to its responses when the user conveys emotions or faces challenging circumstances?",
    "scoreNO_description": "The model neglects to identify or react to the emotional tone of user inputs, giving responses that are unfitting or emotionally insensitive.",
    "scoreYES_description": "The model excels in identifying emotional context and persistently offers empathetic, emotionally aware responses that demonstrate a profound comprehension of the user's emotions or situation.",
}

score_rubric = BINARY_RUBRIC_TEMPLATE.format(**rubric_data)


feedback, score = judge.single_binary_grade(
    instruction=instruction,
    response=response,
    rubric=score_rubric,
)

print("Feedback:", feedback)
print("Score:", score)
