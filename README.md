# langchain_readlocal
Uses langchain to read local files into vector database and begin Q&A with LLM using the vectorized documents 

### How to Use
- User is required to install python packages from the requirements.txt file, the python version used is: Python 3.11.4
- User is required to switch out the gpt4all.py file from the gpt4all folder installed at the module's location with the one provided, the difference is that the one provided here ensures the LLM acts locally and with the model of the user's choice rather than the default model that will be installed from gpt4all's website. This allows the LLM to run purely locally and without the need of internet connection. Note the user is required 2 inputs into the gpt4all.py file (the file location of the LLM used and the name of the file itself)
- This means the user will need to download a LLM of their choice "xx.bin" (can find many online with ease) and insert the file location and its name into the gpt4all.py file as well as main.py
- The user also needs an openai api key for usage

# Roadmap
- [x] Q&A and document fetching works as intended
- [ ] Increase efficiency + customization: allow users to select specific pages of documents
- [ ] Increase efficiency + customization: allow users to search documents for specific words and disregard sections without
- [ ] Test out different models and compile a list comparing accuracy, file size and speed (some models are very slow and don't provide much more accuracy)
- [ ] Make code more interactable and user-friendly
