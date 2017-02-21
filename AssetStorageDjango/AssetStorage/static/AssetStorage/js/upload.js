const tagbox = document.querySelector('.tag-box')
const taglist = document.querySelector('.tag-list')
let tags = taglist.querySelectorAll('.tag-text')
const upload = document.getElementById('upload');
const tagInput = document.getElementById('asset-tags');
let closeButtons = document.querySelectorAll('.tag-close');
const triggers = document.querySelectorAll('.trigger');

triggers.forEach(trigger => trigger.addEventListener('click', triggerInput))
closeButtons.forEach(button => button.addEventListener('click', removeTag));
tagbox.addEventListener('click', addTag);
upload.addEventListener('click', collectTags);

//TODO upload animation [ ]
//TODO change text and display after upload to show file accepted [ ]
function triggerInput(e) {
	e.preventDefault();
	console.log('triggering input')
	this.nextElementSibling.click();
}

function removeTag() {
	this.parentElement.remove();
}

function removeBlankTag() {
	if (!this.textContent) {
		this.parentElement.remove();
	}
}

function addTag(e) {
	if (e.target === tagbox || e.target === taglist) {
		let newli = document.createElement('li');
		let newtext = document.createElement('span');
		let newprediction = document.createElement('span');
		let newclose = document.createElement('div');
		let newx = document.createElement('span');
		
		newli.className = 'tag-container';
		newtext.className = 'tag-text';
		newclose.className = 'tag-close';
		newprediction.className = 'tag-predict';
		
		newtext.setAttribute('contenteditable', 'true');
		newtext.setAttribute('tagindex', 1);
		
		newclose.addEventListener('click', removeTag);
		newtext.addEventListener('blur', removeBlankTag);
		newtext.addEventListener('keydown', tagFinished);
		newtext.addEventListener('keyup', displayMatch);
		
		newx.textContent = 'x';

		newli.append(newtext);
		newli.append(newprediction);
		newli.append(newclose);
		newclose.append(newx);
		taglist.append(newli);
		newtext.focus();
	}
}

function tagFinished(e) {
	if (e.code === 'Tab' || e.code === 'Enter') {
		e.preventDefault();
		prediction = this.nextSibling;
		this.textContent += prediction.textContent;
		prediction.textContent = '';
		addTag({target: tagbox});	
	}
}

function collectTags() {
	console.log('collecting tags');
	let tagl = taglist.querySelectorAll('.tag-text');
	let tagarray = [...tagl].reduce( (acc, val) => 
	{
		console.log('adding ' + val + ' to array');
		if ( !val.textContent) {
			return acc;
		}
		newval = val.textContent.trim()
		console.log(newval);
		acc.push(newval);
		console.log(acc);
		return acc;
	}, 
	[]);
	
	console.log(tagarray);
	tagInput.value = tagarray;
}

function findMatches(wordToMatch, matchSet) {
	return matchSet.filter(phrase => {
		const regex = new RegExp('^' + wordToMatch, 'gi');
		return phrase.match(regex);
	})
}

function uploadAsset(e) {
	e.preventDefault();
	collectTags();
	this.submit();
}
//TODO check for empty string [X]
//TODO normalize caps lock [ ]
//TODO remove duplicates [ ]
//TODO autocomplete on click away [ ]
//TODO smoosh together predictive on submit [ ]
//TODO shift tab between tags [ ]

function displayMatch() {
	// current_tags is currently written into the django template
	//could rewrite so that it is pulled in via ajax
	let search = this.textContent;
	matches = findMatches(search, current_tags);
	if (matches.length === 0 || search === ''){
		this.nextSibling.textContent = ''
		return;
	}
		this.nextSibling.textContent = matches[0].replace(search, '');
	
  // const match = findMatches(this.value, cities)[0];
  
}

