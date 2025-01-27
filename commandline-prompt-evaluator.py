import csv
import os
import sys
from openai import OpenAI
import sys
client = OpenAI()

# Set your OpenAI API key (for example from environment variable)
client = OpenAI(api_key=os.getenv("API_KEY_HERE"))
prompt_input = sys.argv[1]

evaluation_criteria = f"""
    Please evaluate the specified prompt in detail according to the following evaluation criteria, assign scores, categorize the prompt, and provide specific feedback and improvement suggestions.

1. Evaluation Criteria
1. Clarity:
• Definition: Is the prompt expressed clearly? Are the sentences fluent and are the instructions unambiguous?
• Scoring Guidelines:
• 5 points: Completely clear, no ambiguity.
• 1 point: Extremely unclear, very vague.
2. Specificity:
• Definition: Is the prompt sufficiently specific? Does it provide adequate background information and details?
• Scoring Guidelines:
• 5 points: Highly specific, includes detailed background and particulars.
• 1 point: Very vague, lacks necessary details.
3. Goal-Oriented:
• Definition: Does the prompt clearly point towards the expected outcome or objective?
• Scoring Guidelines:
• 5 points: Clearly defined goal, strong direction.
• 1 point: Vague or unclear objective.
4. Creativity:
• Definition: Does the prompt encourage innovative and diverse responses?
• Scoring Guidelines:
• 5 points: Highly innovative, stimulates a variety of responses.
• 1 point: Lacks creativity, responses are likely to be monotonous.
5. Appropriateness:
• Definition: Is the prompt content suitable for the target audience and usage scenario?
• Scoring Guidelines:
• 5 points: Highly appropriate, aligns well with the target audience and context.
• 1 point: Inappropriate, mismatches with audience or context.
6. Actionability:
• Definition: Can the prompt guide specific, actionable responses?
• Scoring Guidelines:
• 5 points: Leads to specific and actionable answers.
• 1 point: Too abstract, difficult to act upon.
7. Language Quality:
• Definition: Are grammar, spelling, and word choice correct and appropriate?
• Scoring Guidelines:
• 5 points: Grammatically correct, no spelling errors, appropriate vocabulary.
• 1 point: Numerous grammatical and spelling errors, poor word choice.

2. Scoring System

• Each criterion is scored on a scale of 1 to 5:
• 5 points: Excellent, fully meets the criterion.
• 4 points: Good, largely meets the criterion.
• 3 points: Average, partially meets the criterion.
• 2 points: Below average, minimally meets the criterion.
• 1 point: Poor, does not meet the criterion.

3. Evaluation Steps

1. Score Each Criterion:
• Assess the prompt against each of the seven criteria and assign a score from 1 to 5 based on the guidelines.
2. Calculate Total Score:
• Sum the scores from all seven criteria to obtain the total score.
3. Categorize the Prompt:
• 31-35 points: Excellent Prompt
• 26-30 points: Good Prompt
• 21-25 points: Average Prompt
• 16-20 points: Below Average Prompt
• 7-15 points: Poor Prompt
4. Provide Quality Feedback and Improvement Suggestions:
• Based on the total score, offer specific feedback and actionable recommendations to enhance the prompt.

4. Evaluation Format

Prompt to be Evaluated:
{prompt_input}

Evaluation Results:

1. Clarity: [Score] / 5
2. Specificity: [Score] / 5
3. Goal-Oriented: [Score] / 5
4. Creativity: [Score] / 5
5. Appropriateness: [Score] / 5
6. Actionability: [Score] / 5
7. Language Quality: [Score] / 5

Total Score: [Total Score] / 35
Category: [Category]

Quality Feedback and Improvement Suggestions:

• [Specific feedback and suggestions for improvement]
    """

def evaluate_with_openai(prompt):

    try:
        # Replace `gpt-4o-mini` with the model you want:
        response = client.chat.completions.create(model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that evaluates data based on given criteria."
            },
            {
                "role": "user",
                "content": prompt
            },
        ],
        temperature=0.7)
        # This is a non-streaming example. If you want streaming, adjust accordingly.
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("[ERROR] OpenAI API call failed:", str(e))
        return "OpenAI call failed. No evaluation."



if __name__ == "__main__":
    print(evaluate_with_openai(evaluation_criteria))
