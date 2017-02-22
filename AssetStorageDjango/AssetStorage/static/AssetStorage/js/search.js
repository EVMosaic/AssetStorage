const tags = document.querySelectorAll('.tag');
const tag_form = document.getElementById('tag-form');
const selected_tags = document.getElementById('selected-tags');
const asset_list = document.querySelector('.asset-list');
const all_assets = document.querySelectorAll('.asset-item');

tags.forEach( tag => tag.addEventListener('click', toggleSelected));

function toggleSelected(){
	console.log('toggling ' + this.textContent);

	if (this.classList.contains('selected')) {
		this.classList.remove('selected');
		removeTag(this);
		if (selected_tags.value === '') {
			clearTags();
			resetAssetList();
		}
	} else {
		this.classList.add('selected');
		appendTag(this);
		console.log(selected_tags.value);
		filterTags();
	}
}

function appendTag(tag) {
	console.log('appending');
	console.log(selected_tags.value);
	// selected_tags.value += tag.dataset.pk + ':';
	selected_tags.value = tag.dataset.tagPk;
	console.log(selected_tags.value);
}

function removeTag(tag) {
	// selected_tags.value = selected_tags.value.replace(tag.dataset.pk + ':', '');
	selected_tags.value = '';
}

function clearTags() {
	tags.forEach(tag => tag.classList.remove('hidden'));
}

function resetAssetList() {
	all_assets.forEach(asset => asset.classList.remove('hidden'));
}

function filterTags() {
	fetch('.', {
		method: 'post',
		credentials: 'include',
		body: new FormData(tag_form)
	})
	.then(function(response) {
		response.json().then(function(json){
			let django_json = JSON.parse(json);
			console.log(django_json);
			clearAssetList();
			// updateAssetList(django_json.assets);
			hideAssets(django_json.assets);
			updateTagList(django_json.tags)
		})
	})
}


function clearAssetList() {
	// asset_list.innerHTML = '';
	all_assets.forEach( asset => asset.classList.add('hidden'));
}


function buildAsset(json_asset) {
	asset_element = document.createElement('div');
	asset_link = document.createElement('a');
	asset_preview = document.createElement('div');
	asset_preview_img = document.createElement('img');
	asset_info = document.createElement('div');
	asset_p = document.createElement('p');
	asset_name = document.createElement('span');
	asset_loc = document.createElement('span');
	asset_size = document.createElement('span');
	
	asset_element.className = 'asset-item';
	asset_preview.className = 'asset-preview';
	asset_info.className = 'asset-info';
	asset_name.className = 'asset-info-item';
	asset_loc.className = 'asset-info-item';
	asset_size.className = 'asset-info-item';

	asset_link.href = `/simple/${json_asset.pk}`;
	asset_preview_img.src = json_asset.thumb;

	asset_name.innerText = `Asset Name: ${json_asset.name}`;
	asset_loc.innerText = `Asset Location: ${json_asset.file}`;
	asset_size.innerText = `Asset Size: ${json_asset.size}`;

	// build tumbnail 
	asset_preview.append(asset_preview_img);
	asset_link.append(asset_preview);
	// build info
	asset_p.append(asset_name);
	asset_p.append(asset_loc);
	asset_p.append(asset_size);

	asset_info.append(asset_p);
	// build asset item
	asset_element.append(asset_link);
	asset_element.append(asset_info);

	return asset_element;
}

function hideAssets(new_assets) {
	asset_elements = []
	new_assets.forEach( asset => {
		// asset_elements.push(buildAsset(asset));
		console.log(asset);
		document.querySelector(`[data-asset-pk="${asset.pk}"]`).classList.remove('hidden');
		console.log(document.querySelector(`[data-asset-pk="${asset.pk}"]`));
	});
}

function updateAssetList(new_assets) {
//think about looking into document fragments here?
	asset_elements = []
	new_assets.forEach( asset => {
		asset_elements.push(buildAsset(asset));
	});
	asset_elements.forEach( element => {
		asset_list.append(element);
	})
}	

function updateTagList(current_tags) {
	tags.forEach( tag => {
		if (!current_tags.includes(parseInt(tag.getAttribute('data-tag-pk')))) {
			tag.classList.add('hidden');
		} else {
			// console.log(`keeping tag number ${tag.getAttribute('data-pk')}`);
			tag.classList.remove('hidden');
		}
	})
}



function getCookie(name) {
       var cookieValue = null;
       if (document.cookie && document.cookie != '') {
         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
             var cookie = cookies[i].trim();
             // Does this cookie string begin with the name we want?
             if (cookie.substring(0, name.length + 1) == (name + '=')) {
                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                 break;
                }
            }
        }
        return cookieValue;
    }