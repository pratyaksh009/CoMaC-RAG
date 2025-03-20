import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
           The scraped text is from the careers page of a website. 
           Your task is to extract job listings and return them in JSON format with the following 
           keys: role, experience, skills, and description. 
                Only return the valid JSON (no extra explanation).
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are the Chief Business Officer at XYZ Company, an AI and Software Consulting firm 
            dedicated to helping businesses integrate their operations seamlessly through automation. 

            Over the years, XYZ has empowered numerous organizations by providing tailored solutions 
            that promote scalability, optimize processes, reduce costs, and enhance overall efficiency.
            Your task is to write a cold email to a potential client, highlighting how XYZ can fulfill 
            their needs by delivering custom solutions that will streamline their business operations.
            
            Also add the most relevant ones from the following links to showcase XYZ's portfolio: {link_list}
            Remember you are CBO at XYZ. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))