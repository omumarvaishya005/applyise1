# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def analyze_job_description(job_desc: str) -> str:
    template = """
You are a job analyst. Extract and list:

1. Technical skills required
2. Soft skills required
3. Years of experience
4. Educational background
5. Any demographic preferences (age, gender, location)
6. Important keywords for a strong resume

Job Description:
{job_description}
"""

    prompt = PromptTemplate(input_variables=["job_description"], template=template)

    # Replace this with your actual OpenAI key
    llm = ChatOpenAI(
        temperature=0,
        openai_api_key="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"
    )

    chain = prompt | llm
    # result = chain.invoke({"input": job_desc})
    result = chain.invoke({"job_description": job_desc})
    return result


if __name__ == "__main__":
    sample_jd = """

About the job

    Carry out on-site installation, configuration, and testing of XDR, SIEM, DLP, SOAR components as per deployment plans
     Perform initial troubleshooting of deployment and integration issues; resolve wherever possible or escalate to L2/L3 teams
     Coordinate with the client's IT, network, and security teams for necessary access, log configurations, and policy enablement
     Ensure proper ingestion of logs, agent installations, network traffic configurations, and data flow for solution effectiveness
     Maintain detailed deployment and issue logs, prepare installation reports, and update project status to the project manager
     Conduct basic training for client IT/security staff on solution operation and basic troubleshooting
     Support acceptance testing and handover documentation
     Follow change management and security best practices during deployment

Required Qualifications and Experience:

     Diploma/Bachelor's Degree in Computer Science, IT, Electronics, or related field
     1-5 years of hands-on experience in deploying or supporting cybersecurity solutions (XDR/EDR, SIEM, DLP, SOAR) or enterprise network security solutions
     Sound knowledge of networking concepts (routing, switching, firewalls, proxy, VPN)
     Working knowledge of operating systems (Windows/Linux) and endpoint security tools
     Ability to analyze logs, troubleshoot connectivity or policy issues, and perform root cause analysis



"""
    output = analyze_job_description(sample_jd)
    print("Extracted Info:\n", output.content)
