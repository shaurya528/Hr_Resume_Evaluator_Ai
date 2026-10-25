import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
import json

load_dotenv()

My_Api_Key=os.getenv("GROQ_API_KEY")

if not My_Api_Key:
    raise ValueError("api key is missing")

Model=os.getenv("Model")
if not Model:
    raise ValueError("model is missing ")
Client=Groq(api_key=My_Api_Key)
class Jobd(BaseModel):
    role: str
    required_skills: list[str]
    preferred_skills: list[str]
    minimum_experience: float | None
    education_requirements: list[str]
    responsibilities: list[str]

Job_Schema=Jobd.model_json_schema()



User_Prompt="""We are looking for an enthusiastic AI Intern who wants to gain practical experience in Artificial Intelligence, Machine Learning, and AI-based application development. The intern will work on real-world projects and collaborate with the technical team.

Key Responsibilities

Assist in developing and testing AI/ML-based applications.
Work with Python for data processing and AI development.
Explore and integrate AI APIs and open-source AI models.
Work on chatbots, automation, and AI-powered applications.
Assist with data collection, preprocessing, and analysis.
Implement basic Machine Learning and Generative AI concepts.
Work with APIs, databases, and AI tools.
Debug, test, and improve AI applications.
Collaborate with team members and contribute to project development.
Document project work and technical processes.
Required Skills

Basic knowledge of Python.
Understanding of AI/ML fundamentals.
Familiarity with APIs and JSON.
Basic knowledge of Git/GitHub.
Problem-solving and analytical skills.
Willingness to learn new AI technologies and tools.
Good to Have

Knowledge of Generative AI, LLMs, RAG, LangChain, or n8n.
Familiarity with OpenAI or open-source models such as Ollama.
Basic knowledge of SQL, FastAPI, or Django.
Experience with GitHub projects.
Eligibility

Students and freshers are eligible to apply.
Candidates pursuing or recently completed B.Tech, B.E., BCA, MCA, M.Tech, or related programs can apply.
Candidates with a basic understanding of Python and AI/ML are preferred.
Prior internship or professional experience is not mandatory.
Candidates with a strong interest in learning and building AI projects are encouraged to apply.
What You Will Gain

Hands-on experience with real-world AI projects.
Practical exposure to AI and automation workflows.
Experience working with development tools and APIs.
Mentorship and guidance from the technical team.
Internship certificate and project experience.
Opportunity to build a strong AI-focused portfolio."""

System_Prompt=f"""
Role: act as a hr for a IT Company
Task: your task is fetch the job description and give the response accoding to the {Job_Schema}
Constraints:Fetch all detail from the Job description not invent anything,Do NOT return the schema itself.Do NOT return fields like "properties", "title" or "type".
Fill the schema with actual information extracted from the job description.
Output: give me response in json and accoding to {Job_Schema}
"""
response=Client.chat.completions.create(model=Model,messages=[{
    "role":"system",
    "content":System_Prompt
},{"role":"user",
    "content":User_Prompt}
    ],response_format={
        "type":'json_object'
    })


answer=response.choices[0].message.content 
Raw_Json=json.loads(answer)
print(Raw_Json["role"])



  



