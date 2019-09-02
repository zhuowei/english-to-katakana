const jpRegex = /(\W|^)(THEREGEX)(ed|es|d|s)?(\W|$)/gi;
const jpMap = THEMAP;

walk(document.body);

function walk(node) 
{
	// I stole this function from here:
	// http://is.gd/mwZp7E
	
	var child, next;
	
	var tagName = node.tagName ? node.tagName.toLowerCase() : "";
	if (tagName == 'input' || tagName == 'textarea') {
		return;
	}
	if (node.classList && node.classList.contains('ace_editor')) {
		return;
	}

	switch ( node.nodeType )  
	{
		case 1:  // Element
		case 9:  // Document
		case 11: // Document fragment
			child = node.firstChild;
			while ( child ) 
			{
				next = child.nextSibling;
				walk(child);
				child = next;
			}
			break;

		case 3: // Text node
			handleText(node);
			break;
	}
}

function handleReplace(match, g1, g2, g3, g4) {
	return g1 + jpMap[g2.toLowerCase()] + (g3 || "") + g4;
}

function handleText(textNode) 
{
	var v = textNode.nodeValue;

	v = v.replace(jpRegex, handleReplace);
	
	textNode.nodeValue = v;
}


