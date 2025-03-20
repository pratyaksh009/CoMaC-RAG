# CoMaC-RAG

CoMaC is a **Generative AI**-powered tool designed to assist service-based companies, business startups, and outsourcing firms in optimizing their cold email outreach efforts. By leveraging advanced AI techniques, CoMaC generates highly personalized and contextually relevant cold emails based on a target company’s website URL.

---

## 🚀 **Features**

- **Contextual Cold Email Generation**: Uses Llama, a Large Language Model (LLM), to craft tailored emails based on the target company’s website.
- **Data Storage & Retrieval**: ChromaDB is employed as a vector database to store and quickly retrieve relevant company data.
- **Orchestrated Workflows**: LangChain is used to orchestrate the entire process of data fetching and processing, ensuring accurate and timely information for email generation.
- **User-Friendly Interface**: Built with Streamlit, providing a simple and interactive interface for users to input the target company’s careers page URL.

---

## 🔧 **Technologies Used**

The following technologies power CoMaC:

- **Llama (LLMs)**: A Large Language Model (LLM) used to generate personalized cold emails based on company data.
- **LangChain**: A framework to orchestrate workflows, fetching and processing relevant data to ensure the accuracy of email generation.
- **ChromaDB**: A vector database for storing and retrieving relevant data to ensure quick access to critical information.
- **Streamlit**: A framework used to create a user-friendly interface, allowing users to easily input and interact with the tool.

---

## 🛠️ **How It Works**

CoMaC works by following these core steps:

1. **User Input**: The user provides the URL of the target company’s careers page.
2. **Data Retrieval**: LangChain fetches relevant data from the website and processes it for email generation.
3. **Email Generation**: Llama generates a highly contextual and personalized cold email based on the target company’s details.
4. **Email Delivery**: The tool generates a draft of the email, ready for review and delivery.

---

## 🖥️ **Getting Started**

To get started with CoMaC, follow the steps below:

### 1. **Clone the repository**

```bash
git clone https://github.com/yourusername/repository-name.git
```
### 2. **Install Dependencies**
```
cd repository-name
pip install -r requirements.txt
```
### 3. **Run the Application**
```
streamlit run app.py
```


