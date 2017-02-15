const tagbox = document.querySelector('.tag-box')
const taglist = document.querySelector('.tag-list')
let tags = taglist.querySelectorAll('.tag-text')
const upload = document.querySelector('#upload');
closeButtons = document.querySelectorAll('.tag-close');

closeButtons.forEach(button => button.addEventListener('click', removeTag));
tagbox.addEventListener('click', addTag);
upload.addEventListener('click', collectTags);

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


function collectTags(e) {
	e.preventDefault();
	let tagl = taglist.querySelectorAll('.tag-text');
	let tagstring = [...tagl].reduce( (acc, val) => 
	{
		if ( !val.textContent) {
			return acc;
		}
		return acc + val.textContent.trim() + ':';
	}, 
	'');
	
	console.log(tagstring);
	return tagstring;
}


function findMatches(wordToMatch, matchSet) {
	return matchSet.filter(phrase => {
		const regex = new RegExp('^' + wordToMatch, 'gi');
		return phrase.match(regex);
	})
}

//TODO check for empty string

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

