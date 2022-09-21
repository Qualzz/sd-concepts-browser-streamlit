import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os

_RELEASE = False

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        "sd_concept_browser ",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component(
        "sd_concept_browser ", path=build_dir)

# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.

st.set_page_config(page_title="Concepts Browser for Stable Diffusion", layout="wide")
def sdConceptsBrowser(concepts, key=None):
	component_value = _component_func(concepts=concepts, key=key, default="")
	return component_value

def getConceptsFromPath(page, conceptPerPage, searchText= ""):
	# get the path where the concepts are stored ->  "./../models/custom/sd-concepts-library"
	path = os.path.abspath(__file__ + "../../../../../models/custom/sd-concepts-library")

	acceptedExtensions = ('jpeg', 'jpg', "png")
	concepts = []

	# List all folders (concepts) in the path
	folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
	filteredFolders = folders

	# Filter the folders by the search text
	if searchText != "":
		filteredFolders = [f for f in folders if searchText.lower() in f.lower()]

	conceptIndex = 1
	for folder in filteredFolders:
		# skip the current folder if it's not within the pagination boudaries
		if conceptIndex < (page - 1) * conceptPerPage or conceptIndex > page * conceptPerPage:
			continue

		concept = {
			"name": folder,
			"token": "<" + folder + ">",
			"images": [],
			"type": ""
		}

		# type of concept is inside type_of_concept.txt
		typePath = os.path.join(path, folder, "type_of_concept.txt")
		if os.path.exists(typePath):
			with open(typePath, "r") as f:
				concept["type"] = f.read()

		# List all files in the concept/concept_images folder
		files = [f for f in os.listdir(os.path.join(path, folder, "concept_images")) if os.path.isfile(os.path.join(path, folder, "concept_images", f))]
		# Retrieve only the 4 first images
		for file in files[:4]:
			if file.endswith(acceptedExtensions):
				# Add a copy of the image to avoid file locking
				originalImage = Image.open(os.path.join(path, folder, "concept_images", file))

				# Maintain the aspect ratio (max 200x200)
				resizedImage = originalImage.copy()
				resizedImage.thumbnail((260, 260), Image.ANTIALIAS)

				#concept["images"].append(resizedImage)

				concept["images"].append(imageToBase64(resizedImage))
				# Close original image
				originalImage.close()

		concepts.append(concept)
		conceptIndex += 1
	return concepts

def conceptGalleryHtml(concepts):
	html = f'<div class="bootstrap-wrapper">'
	html += f'<div class="bootstrap-wrapper concept-gallery row">'
	for concept in concepts:
		html += f'<div class="bootstrap-wrapper concept col-xs-12 col-sm-12 col-md-6 col-lg-4 col-xl-3">'
		html += f'<div class="concept-name">{concept["name"]}</div>'
		html += f'<div class="concept-type">{concept["type"]}</div>'
		html += f'<div class="concept-images">'
		for image in concept["images"]:
			html += f'<img src="data:image/png;base64,{imageToBase64(image)}">'
		html += f'</div>'
		html += f'<div class="concept-token">{concept["token"].replace(">", "&gt;").replace("<", "&lt;")}</div>'
		html += f'</div>'
	html += f'</div>'
	html += f'</div>'


	return html

def imageToBase64(image):
	import io
	import base64
	buffered = io.BytesIO()
	image.save(buffered, format="PNG")
	img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
	return img_str

def layout():
	with st.form("conceptsGallery"):
		# Pagination
		page = 1
		conceptPerPage = 12

		# Search handler
		search_input_col1, search_btn_col1 = st.columns([4,2])

		with search_input_col1:
			searchInput = st.text_input("Search","", placeholder="Search for a concept")

			# Every form must have a submit button, the extra blank spaces is a temp way to align it with the input field. Needs to be done in CSS or some other way.
			search_btn_col1.write("")
			search_btn_col1.write("")
			search_btn = search_btn_col1.form_submit_button("Search")

		placeholder = st.empty()
		# populate the grid with the concepts
		if search_btn or searchInput == "":
			with placeholder.container():
				# Init session state
				if not "concepts" in st.session_state:
					st.session_state['concepts'] = []

				# Refresh concepts
				st.session_state['concepts'] = getConceptsFromPath(page, conceptPerPage, searchInput)
				conceptsLenght = len(st.session_state['concepts'])
				print("Number of concept matching the query:", conceptsLenght)
				copy_to_clipboard_data = sdConceptsBrowser(st.session_state['concepts'], key="clipboard")
				st.markdown(copy_to_clipboard_data, unsafe_allow_html=True)

layout()