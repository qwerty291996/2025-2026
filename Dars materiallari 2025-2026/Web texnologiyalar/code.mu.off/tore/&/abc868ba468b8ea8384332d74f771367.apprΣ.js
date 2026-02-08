(async (π)=>{
	await (async (π)=>{
	await (async (π)=>{
	if (!window.$) {
	window.$ = {};
}
$.norm = true;

if (!window.f) {
	window.f = {};
}

String.prototype.meplace = function(vFrom, vTrom) {
	let vText = this;
	
	while (vText.includes(vFrom)) {
		vText = vText.replace(vFrom, vTrom);
	}
	
	return vText;
}

String.prototype.ucFirst = function() {
	return this[0].toUpperCase() + this.slice(1);
}
String.prototype.lcFirst = function() {
	return this[0].toLowerCase() + this.slice(1);
}
String.prototype.ucSnake = function() {
	let avWord = this.split('_');
	
	let vRess = '';
	
	for (let vWord of avWord) {
		vRess += vWord.ucFirst();
	}
	
	return vRess;
}
String.prototype.ucKebab = function() {
	let avWord = this.split('-');
	
	let vRess = '';
	
	for (let vWord of avWord) {
		vRess += vWord.ucFirst();
	}
	
	return vRess;
}

window.f.aK = function(uxData) {
	return Object.keys(uxData);
}
window.f.aV = function(uxData) {
	return Object.values(uxData);
}
window.f.aC = function(amColl, auxData) {
	let axRess = [];
	
	for (let uxData of auxData) {
		let xTemp = uxData;
		
		for (let mColl of amColl) {
			if (xTemp[mColl] !== undefined) {
				xTemp = xTemp[mColl];
			} else {
				console.error(`no mColl ${mColl} in`, xTemp);
				break;
			}
		}
		
		axRess.push(xTemp);
	}
	
	return axRess;
}

window.f.toJ = function(xData) {
	return JSON.stringify(xData);
}
window.f.toX = function(jData) {
	return JSON.parse(jData);
}



window.f.genI = function(nLeng = 32) {
	function getR(nLeng, vChars) {
		let vRes = '';
		
		for (let i = nLeng; i > 0; --i) {
			vRes += vChars[Math.floor(Math.random() * vChars.length)];
		}
		
		return vRes;
	}
	
	return getR(nLeng, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ');
}
})({}); 

Object.defineProperty(HTMLElement.prototype, 'text', {
	get() {
		return this.textContent;
	},
	set(vText) {
		this.textContent = vText;
	}
});
Object.defineProperty(HTMLElement.prototype, 'hext', {
	get() {
		return this.innerHTML;
	},
	set(vHext) {
		this.innerHTML = vHext;
	}
});
Object.defineProperty(HTMLElement.prototype, 'vext', {
	get() {
		return this.value;
	},
	set(vText) {
		this.value = vText;
	}
});

Object.defineProperty(HTMLElement.prototype, 'tagLame', {
	get() {
		return this.tagName.toLowerCase();
	},
});

return '+';
})({});
await (async (π)=>{
	window.cYell = await (async (π)=>{
	return class cYell {
	constructor(aeDomm, mCatr = null) {
		this.aeDomm = aeDomm;
		this.ueDomm = this.conUE(aeDomm, mCatr);
	}
	
	getE(mDomm = '') {
		if (!mDomm) {
			return this.aeDomm[0];
		} else {
			let eDomm = this.ueDomm[mDomm];
			
			if (eDomm) {
				return eDomm;
			} else {
				return null;
			}
		}
	}
	
	getA() {
		return this.aeDomm;
	}
	
	getU() {
		return this.ueDomm;
	}
	
	getD(mProp, vRarv) {
		return this.getE().getD(mProp);
	}
	getP(mProp, vRarv) {
		return this.getE().getP(mProp);
	}
	setD(mProp, vRarv) {
		for (let eDomm of this.aeDomm) {
			eDomm.setD(mProp, vRarv);
		}
	}
	setP(mProp, vRarv) {
		for (let eDomm of this.aeDomm) {
			eDomm.setP(mProp, vRarv);
		}
	}
	togP(mProp) {
		for (let eDomm of this.aeDomm) {
			eDomm.togP(mProp);
		}
	}
	
	hasP(mProp) {
		for (let eDomm of this.aeDomm) {
			if (!eDomm.hasP(mProp)) {
				return false;
			}
		}
		
		return true;
	}
	hasD(mProp) {
		for (let eDomm of this.aeDomm) {
			if (!eDomm.hasD(mProp)) {
				return false;
			}
		}
		
		return true;
	}
	istP(mProp) {
		for (let eDomm of this.aeDomm) {
			if (!eDomm.istP(mProp)) {
				return false;
			}
		}
		
		return true;
	}
	isfP(mProp) {
		for (let eDomm of this.aeDomm) {
			if (!eDomm.isfP(mProp)) {
				return false;
			}
		}
		
		return true;
	}
	
	conUE(aeDomm, mCatr) {
		if (mCatr) {
			if (aeDomm.length > 0) {
				if (aeDomm[0].hasD(mCatr)) {
					let ueDomm = {};
					
					for (let eDomm of aeDomm) {
						if (eDomm.hasD(mCatr)) {
							let vDatr = eDomm.getD(mCatr);
							ueDomm[vDatr] = eDomm;
						} else {
							throw new Error(`tag needs ${mCatr} attribute`);
						}
					}
					
					return ueDomm;
				}
			} else {
				return {};
			}
		} else {
			return null;
		}
	}

}
})({});
let oDatr = await (async (π)=>{
	if ($.norm === undefined) throw new Error('error: need $.norm in "^/⊙/datr.lib/oDatrΣ.js"');

return new class cDatr {
	constructor() {
		this.auvVarr = {
			'╌': '',
			'⋯': 'g',
			'⊸': 'l',
			'⇢': 'c',
			'≁': 's',
		};
	}
	
	// common selector
	conC(vText) {
		vText = this.conP(vText);
		vText = this.conL(vText);
		vText = this.conB(vText);
		vText = this.conT(vText);
		vText = this.conD(vText);
		
		return vText;
	}
	
	// двоеточие в css
	conP(vText) {
		vText = vText.replace(/(:[a-z-]+)/gi, function(vMach0, vMach1) {
			let uvChen = {
				':fc': ':first-child',
				':lc': ':last-child',
				':oc': ':only-child',
				':nc': ':nth-child',
				':nlc': ':nth-last-child',
				':n': ':not',
				':e': ':empty',
				':a': ':active',
				':l': ':link',
				':v': ':visited',
				':h': ':hover',
				':f': ':focus',
				':B': '::before',
				':A': '::after',
			};
			
			if (uvChen[vMach1]) {
				return uvChen[vMach1];
			} else {
				return vMach1;
			}
		});
		
		return vText;
	}
	
	// for HTML text
	conH(vText) {
		vText = vText.replace(/(╌|⋯|⊸|⇢|≁)(e|s)="(.+?)"/g, (vMach0, vMach1, vMach2, vMach3) => {
			return 'data-' + this.auvVarr[vMach1] + vMach2 + '="' +  vMach3 + '" data-x';
		});
		
		vText = this.conD(vText);
		
		return vText;
	}
	// plain attr
	conD(vText) {
		return vText.replace(/(╌|⋯|⊸|⇢|≁)/g, (vMach0, vMach1) => {
			return 'data-' + this.auvVarr[vMach1];
		});
	}
	
	// tag selector
	conT(vText) {
		return vText.replace(/\[╌t="(.+?)"\]/g, '$1:not([data-x])');
	}
	
	// conv brackets
	conB(vText) {
		return vText.replace(/⁅/g, '> [').replace(/⁆/g, ']');
	}
	
	// for less
	conL(vText) {
		return vText.replace(/μ/g, '_mu');
	}
}


})({});

for (let eExem of [HTMLElement.prototype, window]) {
	eExem.on = function(mEvnt, fCorb) {
		this.addEventListener(mEvnt, function(oEvnt) {
			fCorb({ eTarg: this, oEvnt });
		});
	}
}
// todo: не будет работать, тк привязан анонимный коллбэк
for (let eExem of [HTMLElement.prototype, window]) {
	eExem.of = function(mEvnt, fCorb) {
		this.removeEventListener(mEvnt, function(oEvnt) {
			fCorb({ eTarg: this, oEvnt });
		});
	}
}

HTMLElement.prototype.getP = function(mProp) {
	return this[cn(mProp)];
}
HTMLElement.prototype.getR = function(mProp, vDeff = null) {
	let vRess = this.getAttribute(cn(mProp));
	
	if (vRess === null && vDeff !== null) {
		return vDeff;
	} else {
		return vRess;
	}
}
HTMLElement.prototype.getD = function(mProp, vDeff = null) {
	let vRess = this.getAttribute(cn(mProp));
	
	if (vRess === null && vDeff !== null) {
		return vDeff;
	} else {
		return vRess;
	}
}
HTMLElement.prototype.setP = function(mProp, vRarv) {
	this[cn(mProp)] = vRarv;
}
HTMLElement.prototype.setR = function(mProp, vRarv) {
	this.setAttribute(cn(mProp), vRarv);
}
HTMLElement.prototype.setD = function(mProp, vRarv) {
	this.setAttribute(cn(mProp), vRarv);
}
HTMLElement.prototype.togP = function(mProp) {
	mProp = cn(mProp);
	this[mProp] = !this[mProp];
}
HTMLElement.prototype.exrP = function(mProp, vDeff = null) {
	mProp = cn(mProp);
	let vRess = this[mProp];
	this[mProp] = '';
	
	if (vRess === null && vDeff !== null) {
		return vDeff;
	} else {
		return vRess;
	}
}
HTMLElement.prototype.exrR = function(mProp, vDeff = null) {
	mProp = cn(mProp);
	let vRess = this.getAttribute(mProp);
	this.removeAttribute(mProp);
	
	if (vRess === null && vDeff !== null) {
		return vDeff;
	} else {
		return vRess;
	}
}
HTMLElement.prototype.remR = function(mProp) {
	return this.removeAttribute(cn(mProp));
}

HTMLElement.prototype.hasP = function(mProp) {
	return this.hasAttribute(mProp);
}
HTMLElement.prototype.hasD = function(mProp) {
	return this.hasAttribute(cn(mProp));
}
HTMLElement.prototype.istP = function(mProp) {
	return this[cn(mProp)] ? true: false;
}
HTMLElement.prototype.isfP = function(mProp) {
	return this[cn(mProp)] ? false: true;
}

document.getE = function(vCelt) {
	return this.querySelector(cs(vCelt));
}
document.getA = function(vCelt) {
	return [...this.querySelectorAll(cs(vCelt))];
}
document.getY = function(vCelt, mCatr) {
	let aeDomm = [...this.querySelectorAll(cs(vCelt))];
	
	if (aeDomm.length > 0) {
		return new cYell(aeDomm, mCatr);
	} else {
		return null;
	}
}
document.getAY = function(vCelt) {
	// todo (в сохран кусочках)
}

HTMLElement.prototype.getE = function(vCelt) {
	let vSelt = cs(vCelt);
	
	if (vCelt[0] === '⁅') {
		let aeChid = this.children;
		
		for (let eChid of aeChid) {
			if (eChid.matches(vSelt)) {
				return eChid;
			}
		}
		
		return null;
	} else {
		return this.querySelector(vSelt);
	}
}
HTMLElement.prototype.getA = function(vCelt) {
	let vSelt = cs(vCelt);
	
	if (vCelt[0] === '⁅') {
		let aeDomm = [];
		let aeChid = this.children;
		
		for (let eChid of aeChid) {
			if (eChid.matches(vSelt)) {
				aeDomm.push(eChid);
			}
		}
		
		return aeDomm;
	} else {
		return [...this.querySelectorAll(vSelt)];
	}
}
HTMLElement.prototype.getU = function(vCelt, mCatr) {
	let aeDomm = this.getA(vCelt);
	let yDomm = new cYell(aeDomm, mCatr);
	return yDomm.getU();
}
HTMLElement.prototype.getY = function(vCelt, mCatr = null) {
	let vSelt = cs(vCelt);
	let aeDomm = [];
	
	if (vCelt[0] === '⁅') {
		let aeChid = this.children;
		
		for (let eChid of aeChid) {
			if (eChid.matches(vSelt)) {
				aeDomm.push(eChid);
			}
		}
	} else {
		aeDomm = [...this.querySelectorAll(vSelt)];
	}
	
	if (aeDomm.length > 0) {
		return new cYell(aeDomm, mCatr);
	} else {
		return null;
	}
}

// depricated
document.crate = function(vHext) {
	console.error('document.crate is depricated');
	let eTmpo = document.createElement('div');
	eTmpo.insertAdjacentHTML('afterBegin', oDatr.conH(vHext));
	return eTmpo.firstElementChild;
}
document.crtE = function(vHext) {
	let eTmpo = document.createElement('div');
	eTmpo.insertAdjacentHTML('afterBegin', oDatr.conH(vHext));
	return eTmpo.firstElementChild;
}
document.conH = function(vHext) {
	return oDatr.conH(vHext);
}

function cs(vCelt) {
	return oDatr.conC(vCelt).replace(/^> /, '');
}
function cn(mProp) {
	return oDatr.conD(mProp.replace(/^~[a-z]-/, ''));
}

return '+';

})({});

let cCokr = await (async (π)=>{
	if ($.norm === undefined) throw new Error('error: need $.norm in "^/⊙/cook.lib/cCokrΣ.js"');

return class cCokr {
	get(mCook) {
		let avMach = document.cookie.match(new RegExp(
			"(?:^|; )" + mCook.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
		));
		
		return avMach ? decodeURIComponent(avMach[1]) : undefined;
	}
	
	/*
		set('user', 'John', {secure: true, 'max-age': 3600});
	*/
	set(mCook, vCook, uxOpt = {}) {
		uxOpt = {
			path: '/',
			...uxOpt
		};
		
		if (uxOpt['expires'] instanceof Date) {
			uxOpt['expires'] = uxOpt['expires'].toUTCString();
		}
		
		let vCookC = encodeURIComponent(mCook) + '=' + encodeURIComponent(vCook);
		
		for (let mOpt in uxOpt) {
			vCookC += '; ' + mOpt;
			
			let vOpt = uxOpt[mOpt];
			
			if (vOpt !== true) {
				vCookC += '=' + vOpt;
			}
		}
		
		document.cookie = vCookC;
	}
	
	rem(mCook) {
		this.set(mCook, '', {
			'max-age': -1
		});
	}
}




})({});
$.oCokr = new cCokr;

$.cTabr = await (async (π)=>{
	return class cTabr {
	constructor() {
		this.uyTabb = {};
		this.iCurr;
	}
	
	addT(iTabb, yTabb) {
		this.uyTabb[iTabb] = yTabb;
	}
	
	setC(iNurr) {
		let yCabb = this.uyTabb[this.iCurr];
		
		if (yCabb) {
			yCabb.setD('╌m-curr', 'F');
		}
		
		let yNabb = this.uyTabb[iNurr];
		
		if (yNabb) {
			yNabb.setD('╌m-curr', 'T');
			this.iCurr = iNurr;
		} else {
			console.log(`error: tabb ${iNurr} not found`);
		}
	}
	
	getC() {
		return this.iCurr;
	}
}
})({});

$.uqC   = await (async (π)=>{
	let uqC = {
	P: '',  // path
	Đ: '',  // domain
	Ṫ: '',  // place
	Ŀ: '',  // lang
	uṼ: '', // вместо ref?
};

if (window.location.href.includes('/code.mu.off/')) {
	uqC.Đ = 'code.mu.off';
	uqC.Ṫ = 'F';
	
	let qHurrP = norm(window.location.pathname);
	let oMach = qHurrP.match(/(.+?\/code\.mu\.off)(\/.+)\.html$/);
	
	if (oMach && oMach[1] && oMach[2]) {
		// window.gLocation.base = oMach[1]; // ???
		uqC.P = oMach[2] + '/';
	} else {
		alert('don\'t change the name of the folder "code.mu.off"');
		
		if(window.stop !== undefined) {
			window.stop();
		} else if (document.execCommand !== undefined) { // для IE
			document.execCommand("Stop", false);
		}
		return;
	}
	
} else {
	uqC.P = window.location.pathname;
	uqC.Đ = window.location.hostname;
	
	if (window.location.origin.endsWith('.loc')) {
		uqC.Ṫ = 'L';
	} else {
		uqC.Ṫ = 'N';
	}
}

uqC.Ŀ  = Ŀ(uqC.P);
uqC.uṼ = uṼ(window.location.search.replace(/\?/, ''));

function norm(qHurrP) {
	return qHurrP.replace(/\\/g, '/');
}

function Ŀ(qHurrP) {
	let oMach = qHurrP.match(/^\/(\w\w)\//);
	
	if (oMach && oMach[1]) {
		return oMach[1];
	} else {
		return null;
	}
}

function uṼ(qHurrŁ) {
	let uqHurrṼ = {};
	
	if (qHurrŁ) {
		let aqHurrŨ = qHurrŁ.split('&');
		
		for (let qHurrŨ of aqHurrŨ) {
			let [qHurrÑ, qHurrṼ] = qHurrŨ.split('=');
			
			uqHurrṼ[qHurrÑ] = qHurrṼ;
		}
	}
	
	return uqHurrṼ;
}

return uqC;


})({});
$.oTorc = await (async (π)=>{
	if ($.uqC === undefined) throw new Error('error: need $.uqC in "^/home/trepachev/projects/php/code.mu.loc/tore/libb/oTorcΣ.js"');

let uuvGorc = await (async (π)=>{
	return {
	'code-result': {
		ru: 'Результат выполнения кода',
		en: 'Result of code execution',
	},
	'open-window': {
		ru: 'открыть в дочернем окне',
		en: 'open in a new child window',
	},
	'categories-filter': {
		ru: 'фильтр категорий',
		en: 'categories filter',
	},
	'task': {
		ru: 'Задача',
		en: 'Task',
	},
	'study-theory-on-those-links': {
		ru: 'Изучите теорию по следующим ссылкам',
		en: 'Learn the theory at the following links',
	},
	
	'back-to-reading' : {
		ru: 'вернутся к чтению страницы',
		en: 'back to reading the page',
	},
	'lesson' : {
		ru: 'урок',
		en: 'lesson',
	},
	'of' : {
		ru: 'из',
		en: 'of',
	},
};



})({});

return new class cTorc {
	trn(mKest) {
		let mLerg = $.uqC.Ŀ;
		
		if (mKest !== null && mKest != undefined) {
			if (mLerg && uuvGorc[mKest] && uuvGorc[mKest][mLerg]) {
				return uuvGorc[mKest][mLerg];
			} else {
				return mKest;
			}
		} else {
			return '';
		}
	}
}




})({});

await (async (π)=>{
	await (async (π)=>{
	window.h = {};

h.copyToClipBoard = function(vData) {
	let eInput = document.createElement('input');
	eInput.value = vData;
	eInput.style.position = 'absolute';
	eInput.style.left = '-300px';
	document.body.append(eInput);
	eInput.select();
	document.execCommand('copy');
	eInput.remove();
}

h.createCommonHref = function(vHref) {
	if ($.uqC.Ṫ === 'F') {
		// todo: тут был window.gLocation.base
		return $.uqC.P + vHref.replace(/\/$/, '') + '.html';
	} else {
		return vHref;
	}
}






})({});
await (async (π)=>{
	let cHigh = await (async (π)=>{
	return class cHigh {
	constructor() {
		this._totalCommands = this._getCommands();
	}
	
	handle(str, mode) {
		
		if (this._totalCommands[mode]) {
			let commands = this._totalCommands[mode];
			
			str = this._decodeHtmlSpecialChars(str);
			
			let clefts = this._getClefts(str);
			
			// костыль
			str = str.replace(/<\?php/g, '%?php');
			str = str.replace(/<\?=/g, '%?=');
			str = str.replace(/\?>/g, '?%');
			
			str = this._merge(this._tokenize({str, commands, mode}));
			str = this._handleClefts(str, clefts);
			str = this._addLineNumbers(str);
			
			// костыль
			str = str.replace(/%\?=/g, '&lt;?=');
			str = str.replace(/%\?php/g, '&lt;?php');
			str = str.replace(/\?%/g, '?&gt;');
			
			// костыль
			str = str.replace(/\/\/!!/g, '//');
		}
		
		return str;
	}
	
	/*
		clefts = [
			{type: "break", shift: 25, order: 1, total: 2, tabs: ""},
		];
		
		console.log(Object.assign([], clefts));
	*/
	_handleClefts(str, clefts) {
		function getFlatChildren(elems) {
			let result = [];
			
			for (let elem of elems) {
				let children = elem.children;
				
				if (children.length !== 0) {
					result = result.concat(getFlatChildren(children));
				} else {
					result.push(elem);
				}
			}
			
			return result;
		}
		
		let div = document.createElement('div');
		div.innerHTML = str;
		
		let children = getFlatChildren(div.children)
		
		let curCleft = clefts.shift();
		let counter = 0;
		
		let i = 0;
		while (curCleft !== undefined && i < children.length) {
			let elem = children[i];
			
			let text = elem.textContent;
			let length = text.length;
			
			if (counter + length >= curCleft.shift) {
				// первый найденный разрыв в токене
					let points = [];
					points.push({...curCleft, indent: curCleft.shift - counter});
				//-
				// проверяем, попадают ли в данный токен еще разрывы
					let j = 0;
					for (let cleft of clefts) {
						if (counter + length >= cleft.shift) {
							points.push({...cleft, indent: cleft.shift - counter});
							j++;
						}
					}
					clefts.splice(0, j);
				//-
				// добавляем спены с разрывами в текст
					let newText = '';
					for (let k = 0; k < points.length; k++) {
						let curr = points[k];
						let prevIndent = points[k - 1] ? points[k - 1].indent : 0;
						
						newText += this._encodeHtmlSpecialChars(text.substring(prevIndent, curr.indent));
						
						if (curr.type === 'break') {
							newText += '<span class="-b -b' + curr.order + curr.total + '"><br><span>' + curr.tabs + '&#9;</span></span>';
						}
						if (curr.type === 'gap') {
							newText += '<span class="-b -g' + curr.total + '">&nbsp;</span>';
						}
					}
					newText += this._encodeHtmlSpecialChars(text.substring(points[points.length - 1].indent)); // добавляем хвост строки
					elem.innerHTML = newText;
				//-
				
				curCleft = clefts.shift();
			}
			
			counter += length;
			i++;
		}
		
		return div.innerHTML;
	}
	
	/*
		cleft - разрыв всей строки, - объект с позицией и типом,
		shift - отступ от начала строки
		
		старое
		let singleChunkSize = 32;
		let zeroChunkSize = 25;
		let chunkSize = 15;
		let tailSize = 6;
		let zeroTailSize = 10;
	*/
	_getClefts(str) {
		let points = [
			{
				value: '[^/][^/] ',
				priority: 0
			},
			{
				value: ' = ', 
				priority: 1
			},
			{
				value: ' \\. ',
				priority: 1
			},
			{
				value: ', ',
				priority: 1
			},
			{
				value: ' \\+ ',
				priority: 1
			},
			{
				value: ' - ',
				priority: 1
			},
			{
				value: ' \\* ',
				priority: 1
			},
			{
				value: ' [^<]\\/ ',
				priority: 1
			},
			{
				value: ' % ',
				priority: 1
			},
			{
				value: ' ?? ',
				priority: 1
			},
			{
				value: ' ? ',
				priority: 1
			},
			{
				value: ' && ',
				priority: 1
			},
			{
				value: ' or ',
				priority: 1
			},
			{
				value: ' and ',
				priority: 1
			},
			{
				value: ' \\|\\| ',
				priority: 1
			},
			{
				value: ' >= ',
				priority: 1
			},
			{
				value: ' <= ',
				priority: 1
			},
			{
				value: ' != ',
				priority: 1
			},
			{
				value: '>',
				priority: 1
			},
			{
				value: ' == ',
				priority: 1
			},
			{
				value: ' === ',
				priority: 1
			},
			{
				value: '\s=\s',
				priority: 1
			},
			{
				value: '\\(\\)',
				priority: 2
			},
			
			/*
			 {
				value: '\\]',
				priority: 2
			},
			{
				value: '\\)',
				priority: 2
			},
			{
				value: '"',
				priority: 3
			},
			{
				value: "'",
				priority: 3
			},
			*/
		];
		
		let hoarder = '';
		let result = [];
		
		let lines = str.split('\n');
		
		for (let i = 0; i < lines.length; i++) {
			let line = lines[i];
			let tabs = this._getTabs(line);
			
			let singleChunkSize = 32;
			let zeroChunkSize = 25;
			let chunkSize = 15;
			
			if (getRealLength(line) > singleChunkSize) {
				let counter = 0;
				let clefts = [];
				
				whileLoop:
				while (getRealLength(line) > chunkSize) {
					let cutLength = counter === 0 ? zeroChunkSize : chunkSize;
					
					let optimum;
					
					for (let point of points) {
						let regExp = new RegExp('^(.{' + (cutLength - 9) + '}.+?' + point.value + ')(.{2,})$', 'i');
						let match = line.match(regExp);
						
						if (match) {
							let length = match[1].length;
							let diff = cutLength - length;
							let mdiff = Math.abs(diff);
							
							if (!optimum || Math.abs(optimum.diff) > mdiff) {
								optimum = {diff: diff, chunck: match[1], rest: match[2]};
							}
							
							if (point.priority === 0 && diff >= -8 && diff <= 5 || point.priority === 1 && diff >= -8 && diff <= 5 || point.priority === 2 && mdiff <= 4) {
								break;
							}
						}
						
					}
					
					if (optimum) {
						counter++;
						hoarder += optimum.chunck;
						line = optimum.rest;
						
						clefts.push({type: 'break', shift: hoarder.length, order: counter, total: '?', tabs: tabs});
						
						continue whileLoop;
					}
					
					break;
					
				}
				
				if (line.length > 0) {
					hoarder += line; // хвост забираем
				}
				
				if (clefts.length > 0) {
					for (let cleft of clefts) {
						cleft.total = counter;
					}
				
					clefts.push({type: 'gap', shift: hoarder.length, total: counter});
				}
				hoarder += '\n'; // добавляем один символ на \n
				result = result.concat(clefts);
			} else {
				hoarder += line + '\n';
			}
		}
		
		return result;
		
		function getRealLength(line) {
			return line.length + line.match(/\t*/)[0].length;
		}
	}
	
	_addLineNumbers(str) {
		let lines = str.split('\n');
		let result = [];
		
		for (let i = 0; i < lines.length; i++) {
			let num = i + 1;
			if (num >= 1 && num <= 9) {
				result.push('<span class="-n -n1"></span>' + lines[i]);
			} else if (num >= 10 && num <= 99) {
				result.push('<span class="-n -n2"></span>' + lines[i]);
			} else if (num >= 100 && num <= 999) {
				result.push('<span class="-n -n3"></span>' + lines[i]);
			} else if (num >= 1000 && num <= 9999) {
				result.push('<span class="-n -n4"></span>' + lines[i]);
			}
		}
		str = result.join('\n');
		
		return str;
	}
	
	_getTabs(str) {
		let tabs;
		let match = str.match(/\t*/);
		
		if (match[0].length > 0) {
			tabs = '&#9;'.repeat(match[0].length);
		} else {
			tabs = '';
		}
		
		return tabs;
	}

	_merge(tokens) {
		let result = '';
		
		for (let token of tokens) {
			if (token.inside) {
				
				result += '<span class="-t -m-' + token.mode + ' -t-' + token.type + '">' + this._merge(token.inside) + '</span>';
			} else {
				let match = this._encodeHtmlSpecialChars(token.match);
				
				if (token.type != '~' && token.type != 'ignore') {
					result += '<span class="-t -m-' + token.mode + ' -t-' + token.type + '">' + match + '</span>';
				} else {
					result += match;
				}
			}
		};
		
		return result;
	}
	
	_decodeHtmlSpecialChars(str) {
		str = str.replace(/&amp;/g, '&');
		str = str.replace(/&lt;/g, '<');
		str = str.replace(/&gt;/g, '>');
		
		return str;
	}
	
	_encodeHtmlSpecialChars(str) {
		str = str.replace(/&/g, '&amp;');
		str = str.replace(/</g, '&lt;');
		str = str.replace(/>/g, '&gt;');
		
		return str;
	}
	
	_tokenize(options) {
		let {commands, str, mode} = options;
		
		let lastIndex = 0;
		let tokens = [];
		
		if (commands.length === 0 || commands[commands.length - 1].type != 'plain') {
			commands.push({
				type: 'plain',
				match: /[\s\S]/,
			});
		}
		
		while (lastIndex < str.length) {
			for (let command of commands) {
				
				let regExp = new RegExp(command.match, command.match.flags + 'y');
				regExp.lastIndex = lastIndex;	
				let pockets = regExp.exec(str);
				
				if (pockets) {
					let match = pockets[0];
					
					if (this._checkVicinity(command, str, match, lastIndex)) {
						
						let token = {type: command.type, match, mode};
						
						if (command.explode) {
							token.inside = this._tokenizeExplode(command.explode, pockets, mode);
							
						} else if (command.inside || command.mode) {
							token.inside = this._tokenizeInside(command, match, mode);
						}
						
						let last = tokens[tokens.length - 1];
						if (last && last.mode === token.mode && last.type === token.type) {
							tokens[tokens.length - 1].match += token.match;
						} else {
							tokens.push(token);
						}
						
						lastIndex += match.length - 1;
						break;
					}
				}
			}
			
			lastIndex++;
		}
		
		return tokens;
	}
	
	// Нельзя уносить в основную функцию, тк ее использует _tokenizeExplode
	_tokenizeInside(command, str, mode) {
		if (command.inside) {
			return this._tokenize({str, commands: command.inside, mode});
		} else if (command.mode) {
			return this._tokenizeMode(command, str);
		}
	}
	
	_tokenizeMode(command, str) {
		if (this._totalCommands[command.mode]) {
			let modeCommands = this._totalCommands[command.mode];
			return this._tokenize({str, commands: modeCommands, mode: command.mode});
		} else {
			// неверно указан язык
		}
	}
	
	_tokenizeExplode(commands, pockets, mode) {
		let result = [];
		
		for (let command of commands) {
			let match = pockets[command.pocket];
			
			if (match) {
				let token = {type: command.type, match, mode};
				token.inside = this._tokenizeInside(command, match, mode);
				
				result.push(token);
			} else {
				// неверное имя кармана
			}
		};
		
		return result;
	}
	
	_checkVicinity(command, str, match, lastIndex) {
		if (this._checkBehind(str, lastIndex, command.behind)) {
			if (this._checkNehind(str, lastIndex, command.nehind)) {
				if (this._checkForward(str, lastIndex + match.length, command.forward)) {
					if (this._checkNorward(str, lastIndex + match.length, command.norward)) {
						return true;
					}
				}
			}
		}
		
		return false;
	}
	
	_checkBehind(str, lastIndex, regExp) {
		if (regExp) {
			let behindStr = str.slice(0, lastIndex);
			return (new RegExp('(?:' + regExp.source + ')$', regExp.flags)).test(behindStr);
		} else {
			return true;
		}
	}
	
	_checkNehind(str, lastIndex, regExp) {
		if (regExp) {
			return !this._checkBehind(str, lastIndex, regExp);
		} else {
			return true;
		}
	}
	
	_checkForward(str, lastIndex, regExp) {
		if (regExp) {
			let forwardStr = str.slice(lastIndex);
			return (new RegExp('^(?:' + regExp.source + ')', regExp.flags)).test(forwardStr);
		} else {
			return true;
		}
	}
	
	_checkNorward(str, lastIndex, regExp) {
		if (regExp) {
			return !this._checkForward(str, lastIndex, regExp);
		} else {
			return true;
		}
	}
	
	_getCommands() {
		let сommands = {};
		let inject = {};

		inject.html = [
			{
				type: 'html-tag',
				match: /<[^\/$][^>\s]*?>/,
			},
			{
				type: 'html-tag',
				match: /<[^\/$][^>\s]*/,
			},
			{
				type: 'html-tag',
				match: /<\/[^>\s$]*?>/,
			},
			
			{
				type: 'html-attribute',
				match: /\b[^\s]+?=/,
			},
		];

		inject.sql = [
			{
				type: 'sql-keyword',
				match: /\b(?:TIME_TO_SEC|SEC_TO_TIME|LEAST|MOD|ABS|ROUND|CEILING|FLOOR|LCASE|LOWER|UCASE|UPPER|SPACE|SUBSTRING|LENGTH|SEPARATOR|INTERVAL|TO_DAYS|DATE_FORMAT|MINUTE_SECOND|HOUR_MINUTE|DAY_HOUR|YEAR_MONTH|HOUR_SECOND|DAY_MINUTE|DAY_SECOND|EXTRACT|DAYOFYEAR|DAYNAME|YEARNAME|YEARWEEK|DAYOFWEEK|WEEKDAY|WEEK|YEAR|MONTH|DAY|DAYOFMONTH|HOUR|MINUTE|SECOND|LTRIM|RTRIM|TRIM|ELT|INSTR|LOCATE|POSITION|REPEAT|REVERSE|SUBSTRING_INDEX|REPLACE|LPAD|RPAD|CONCAT_WS|GROUP_CONCAT|CONCAT|SQRT|SIGN|ACTION|ADD|AFTER|ALGORITHM|ALL|ALTER|ANALYZE|ANY|APPLY|ASC|AS|as|AUTHORIZATION|BACKUP|BDB|BEGIN|BERKELEYDB|BIGINT|BINARY|BIT|BLOB|BOOL|BOOLEAN|BREAK|BROWSE|BTREE|BULK|BY|CALL|CASCADED?|CASE|CHAIN|CHAR VARYING|CHARACTER (?:SET|VARYING)|CHARSET|CHECK|CHECKPOINT|CLOSE|CLUSTERED|COALESCE|COLLATE|COLUMN|COLUMNS|COMMENT|COMMIT|COMMITTED|COMPUTE|CONNECT|CONSISTENT|CONSTRAINT|CONTAINS|CONTAINSTABLE|CONTINUE|CONVERT|CREATE|CROSS|CURRENT(?:_DATE|_TIME|_TIMESTAMP|_USER)?|CURSOR|DATA(?:BASES?)?|DATETIME|DBCC|DEALLOCATE|DEC|DECIMAL|DECLARE|DEFAULT|DEFINER|DELAYED|DELETE|DENY|DESC|DESCRIBE|DETERMINISTIC|DISABLE|DISCARD|DISK|DISTINCT|DISTINCTROW|DISTRIBUTED|DO|DOUBLE(?: PRECISION)?|DROP|DUMMY|DUMP(?:FILE)?|DUPLICATE KEY|ELSE|ENABLE|ENCLOSED BY|END|ENGINE|ENUM|ERRLVL|ERRORS|ESCAPE(?:D BY)?|EXCEPT|EXEC(?:UTE)?|EXISTS|EXIT|EXPLAIN|EXTENDED|FETCH|FIELDS|FIELD|FILE|FILLFACTOR|FIRST|FIXED|FLOAT|FOLLOWING|FOR(?: EACH ROW)?|FORCE|FOREIGN|FREETEXT(?:TABLE)?|FROM|FULL|FUNCTION|GEOMETRY(?:COLLECTION)?|GLOBAL|GOTO|GRANT|GROUP|HANDLER|HASH|HAVING|HOLDLOCK|IDENTITY(?:_INSERT|COL)?|IF|IGNORE|IMPORT|INDEX|INFILE|INNER|INNODB|INOUT|INSERT|INT|INTEGER|INTERSECT|INTO|INVOKER|ISOLATION LEVEL|JOIN|KEYS?|KILL|LANGUAGE SQL|LAST|LEFT|LIMIT|LINENO|LINES|LINESTRING|LOAD|LOCAL|LOCK|LONG(?:BLOB|TEXT)|MATCH(?:ED)?|MEDIUM(?:BLOB|INT|TEXT)|MERGE|MIDDLEINT|MODIFIES SQL DATA|MODIFY|MULTI(?:LINESTRING|POINT|POLYGON)|NATIONAL(?: CHAR VARYING| CHARACTER(?: VARYING)?| VARCHAR)?|NATURAL|NCHAR(?: VARCHAR)?|NEXT|NO(?: SQL|CHECK|CYCLE)?|NONCLUSTERED|NULLIF|NUMERIC|OFF?|OFFSETS?|ON|OPEN(?:DATASOURCE|QUERY|ROWSET)?|OPTIMIZE|OPTION(?:ALLY)?|ORDER|OUT(?:ER|FILE)?|OVER|PARTIAL|PARTITION|PERCENT|PIVOT|PLAN|POINT|POLYGON|PRECEDING|PRECISION|PREV|PRIMARY|PRINT|PRIVILEGES|PROC(?:EDURE)?|PUBLIC|PURGE|QUICK|RAISERROR|READ(?:S SQL DATA|TEXT)?|REAL|RECONFIGURE|REFERENCES|RELEASE|RENAME|REPEATABLE|REPLICATION|REQUIRE|RESTORE|RESTRICT|RETURNS?|REVOKE|RIGHT|ROLLBACK|ROUTINE|ROW(?:COUNT|GUIDCOL|S)?|RTREE|RULE|SAVE(?:POINT)?|SCHEMA|SELECT|SERIAL(?:IZABLE)?|SESSION(?:_USER)?|SET(?:USER)?|SHARE MODE|SHOW|SHUTDOWN|SIMPLE|SMALLINT|SNAPSHOT|SOME|SONAME|START(?:ING BY)?|STATISTICS|STATUS|STRIPED|SYSTEM_USER|TABLES?|TABLESPACE|TEMP(?:ORARY|TABLE)?|TERMINATED BY|TEXT(?:SIZE)?|THEN|TIMESTAMP|TINY(?:BLOB|INT|TEXT)|TOP?|TRAN(?:SACTIONS?)?|TRIGGER|TRUNCATE|TSEQUAL|TYPES?|UNBOUNDED|UNCOMMITTED|UNDEFINED|UNION|UNIQUE|UNPIVOT|UPDATE(?:TEXT)?|USAGE|USE|USER|USING|VALUES?|VAR(?:BINARY|CHAR|CHARACTER|YING)|VIEW|WAITFOR|WARNINGS|WHEN|WHERE|WHILE|WITH(?: ROLLUP|IN)?|WORK|WRITE(?:TEXT)?|AND|BETWEEN|IN|LIKE|NOT|OR|IS|DIV|REGEXP|RLIKE|SOUNDS LIKE|XOR|SUM|AVG|MIN|MAX|COUNT|SIGN|MID|DATE|NOW)\b/,
				
			},
		];
		
		сommands.sql = [
			{
				type: 'string',
				match: /('|"|`)\1/,
			},
			{
				type: 'string',
				match: /('|").*?[^\\]\1/,
			},
			{
				type: 'escape',
				match: /`.*?`/,
			},
			{
				type: 'as',
				match: /as/,
			},
			{
				type: 'function',
				match: /[A-Z_]+/,
				forward: /\(/,
			},
			{
				type: 'keyword',
				match: /[A-Z_]+/,
			},
		];

		сommands.html = [
			{
				type: 'php',
				match: /(%\?=|%\?php)([\s\S]*?)(\?%)/,
				explode: [
					{
						type: 'php-open',
						pocket: 1,
					},
					{
						type: 'php',
						pocket: 2,
						mode: 'php',
					},
					{
						type: 'php-close',
						pocket: 3,
					},
				],
			},
			{
				type: 'php',
				match: /(%\?php)([\s\S]*)/,
				explode: [
					{
						type: 'php-open',
						pocket: 1,
					},
					{
						type: 'php',
						pocket: 2,
						mode: 'php',
					},
				],
			},
			
			{
				type: 'comment',
				match: /<!--[\s\S]*?-->/,
			},
			{
				type: 'tag',
				match: /(<style.*?>)([\s\S]*?)(<\/style>)/,
				explode: [
					{
						type: 'tag-name',
						pocket: 1,
					},
					{
						type: '~',
						pocket: 2,
						mode: 'css',
					},
					{
						type: 'tag-name',
						pocket: 3,
					},
				],
			},
			
			{
				type: 'tag',
				match: /(<script.*?>)([\s\S]*?)(<\/script>)/,
				explode: [
					{
						type: 'tag-name',
						pocket: 1,
					},
					{
						type: '~',
						pocket: 2,
						mode: 'javascript',
					},
					{
						type: 'tag-name',
						pocket: 3,
					},
				],
			},
			{
				type: 'tag-name',
				match: /<[^\/][^>\s]*?>/,
			},
			{
				type: 'tag-name',
				match: /<\/[^>\s]*?>/,
			},
			{
				type: 'tag',
				match: /(<[^\/][^>]*?)(\s+)([^>]*?)(\s*)(>)/,
				explode: [
					{
						type: 'tag-name',
						pocket: 1,
					},
					{
						type: 'gap',
						pocket: 2,
					},
					{
						type: 'attributes',
						pocket: 3,
						inside: [
							{
								type: 'attribute',
								nehind: /</,
								match: /(on[^\s]+?)(\s*)(=)(\s*)("|')([\s\S]*?)(\5)/,
								explode: [
									{
										type: 'name',
										pocket: 1,
									},
									{
										type: 'gap',
										pocket: 2,
									},
									{
										type: 'equal',
										pocket: 3,
									},
									{
										type: 'gap',
										pocket: 4,
									},
									{
										type: 'quote',
										pocket: 5,
									},
									{
										type: 'javascript',
										pocket: 6,
										mode: 'javascript',
									},
									{
										type: 'quote',
										pocket: 7,
									},
								],
							},
							{
								type: 'attribute',
								nehind: /</,
								match: /([^\s]+?)(\s*)(=)(\s*)("|')([\s\S]*?)(\5)/,
								explode: [
									{
										type: 'name',
										pocket: 1,
									},
									{
										type: 'gap',
										pocket: 2,
									},
									{
										type: 'equal',
										pocket: 3,
									},
									{
										type: 'gap',
										pocket: 4,
									},
									{
										type: 'quote',
										pocket: 5,
									},
									{
										type: 'value',
										pocket: 6,
										inside: [
											{
												type: 'php',
												match: /(%\?=|%\?php)([\s\S]*?)(\?%)/,
												explode: [
													{
														type: 'php-open',
														pocket: 1,
													},
													{
														type: 'php',
														pocket: 2,
														mode: 'php',
													},
													{
														type: 'php-close',
														pocket: 3,
													},
												],
											},
										],
									},
									{
										type: 'quote',
										pocket: 7,
									},
								],
							},
							{
								type: 'php',
								match: /(%\?=|%\?php)([\s\S]*?)(\?%)/,
								explode: [
									{
										type: 'php-open',
										pocket: 1,
									},
									{
										type: 'php',
										pocket: 2,
										mode: 'php',
									},
									{
										type: 'php-close',
										pocket: 3,
									},
								],
							},
							
							{
								type: 'property',
								nehind: /</,
								match: /\b[^\s<>"']+?\b/,
							},
						],
					},
					{
						type: 'gap',
						pocket: 4,
					},
					{
						type: 'tag-name',
						pocket: 5,
					},
				],
			},
		];
		
		сommands.xml = [
			{
				type: 'tag-name',
				match: /<[^\/][^>\s]*?>/,
			},
			{
				type: 'tag-name',
				match: /<\/[^>\s]*?>/,
			},
			{
				type: 'tag',
				match: /(<[^\/][^>]*?)(\s+)([^>]*?)(\s*)(>)/,
				explode: [
					{
						type: 'tag-name',
						pocket: 1,
					},
					{
						type: 'gap',
						pocket: 2,
					},
					{
						type: 'attributes',
						pocket: 3,
						inside: [
							{
								type: 'attribute',
								nehind: /</,
								match: /([^\s]+?)(\s*)(=)(\s*)("|')([\s\S]*?)(\5)/,
								explode: [
									{
										type: 'name',
										pocket: 1,
									},
									{
										type: 'gap',
										pocket: 2,
									},
									{
										type: 'equal',
										pocket: 3,
									},
									{
										type: 'gap',
										pocket: 4,
									},
									{
										type: 'quote',
										pocket: 5,
									},
									{
										type: 'value',
										pocket: 6,
									},
									{
										type: 'quote',
										pocket: 7,
									},
								],
							},
							{
								type: 'property',
								nehind: /</,
								match: /\b[^\s<>"']+?\b/,
							},
						],
					},
					{
						type: 'gap',
						pocket: 4,
					},
					{
						type: 'tag-name',
						pocket: 5,
					},
				],
			},
		];
		
		сommands.blade = [
			...сommands.html,
			{
				type: 'command',
				match: /@(foreach|endforeach|for|endfor|if|endif|elseif|forelse|endforelse|empty|break|continue|php|endphp)\b/,
			},
			
		];
		
		сommands.css = [
			{
				type: 'comment',
				match: /\/\*[\s\S]*?\*\//,
			},
			{
				type: 'command',
				match: /@(?:(?:-webkit-|-moz-|-o-)?keyframes|support)/,
			},
			{
				type: 'property',
				match: /([a-zA-Z-]+?|@\{[a-zA-Z0-9_-]+?\})(\s*)(:)(\s*)(.+?)(;)/,  // todo: не светит переменные в именах свойств
				explode: [
					{
						type: 'name',
						pocket: 1,
					},
					{
						type: 'gap',
						pocket: 2,
					},
					{
						type: 'punctuation',
						pocket: 3,
					},
					{
						type: 'gap',
						pocket: 4,
					},
					{
						type: 'value',
						pocket: 5,
						inside: [
							{
								type: 'string',
								match: /('|").*?\1/,
							},
							{
								type: 'function',
								match: /[a-zA-Z0-9_-]+/,
								forward: /\(/,
							},
						],
					},
					{
						type: 'punctuation',
						pocket: 6,
					},
				],
			},
			{
				type: 'media',
				match: /(@media)(\s+)((?:\(.+?\)(?:\s+(?:and)\s)?)+)(\s*)/,
				behind: /[\t ]*/,
				forward: /\{/,
				explode: [
					{
						type: 'name',
						pocket: 1,
					},
					{
						type: 'gap',
						pocket: 2,
					},
					{
						type: '~',
						pocket: 3,
						inside: [
							{
								type: 'bracket',
								match: /[\(\)]/,
							},
							{
								type: 'punctuation',
								match: /:/,
							},
							{
								type: 'command',
								match: /max-width|min-width/,
							},
							{
								type: 'condition',
								match: /and/,
							},
						],
					},
					{
						type: 'gap',
						pocket: 4,
					},
				],
			},
			{
				type: 'selector',
				behind: /[\t ]*/,
				match: /[^{}\n\/]+/,
				forward: /\s*\{/,
				inside: [
					{
						type: 'punctuation',
						match: /[,+>~]/,
					},
					{
						type: 'bracket',
						match: /[()]/,
					},
					{
						type: 'attribute',
						match: /(\[)([a-z-]+)(\])/,
						explode: [
							{
								type: 'bracket',
								pocket: 1,
							},
							{
								type: 'name',
								pocket: 2,
							},
							{
								type: 'bracket',
								pocket: 3,
							},
						],
					},
					{
						type: 'attribute',
						match: /(\[)([a-z-]+)(\s*)([|$*~|^]?=)(\s*)(["'])([a-z-]+)(\6)(\])/,
						explode: [
							{
								type: 'bracket',
								pocket: 1,
							},
							{
								type: 'name',
								pocket: 2,
							},
							{
								type: 'gap',
								pocket: 3,
							},
							{
								type: 'operator',
								pocket: 4,
							},
							{
								type: 'gap',
								pocket: 5,
							},
							{
								type: 'quote',
								pocket: 6,
							},
							{
								type: 'value',
								pocket: 7,
							},
							{
								type: 'quote',
								pocket: 8,
							},
							{
								type: 'bracket',
								pocket: 9,
							},
						],
					},
					{
						type: 'function',
						match: /::?[a-z-]+/,
						forward: /\(/,
					},
					{
						type: 'pseudo',
						match: /::?[a-z-]+/,
						norward: /\(/,
					},
					{
						type: 'id',
						match: /#[a-z0-9_-]+/i,
					},
					{
						type: 'class',
						match: /\.[a-z0-9_-]+/i,
					},
				]
			},
			{
				type: 'bracket',
				match: /\{\}/,
			},
			
		];

		сommands.scss = [
			{
				type: 'comment',
				match: /\/\/.*/,
			},
			{
				type: 'comment',
				match: /\/\*[\s\S]*?\*\//,
			},
			{
				type: 'command',
				match: /@(?:(?:-webkit-|-moz-|-o-)?keyframes|support)/,
			},
			{
				type: 'media',
				match: /(@media)(\s+)((?:\(.+?\)(?:\s+(?:and)\s)?)+)(\s*)/,
				behind: /[\t ]*/,
				forward: /\{/,
				explode: [
					{
						type: 'name',
						pocket: 1,
					},
					{
						type: 'gap',
						pocket: 2,
					},
					{
						type: '~',
						pocket: 3,
						inside: [
							{
								type: 'bracket',
								match: /[\(\)]/,
							},
							{
								type: 'punctuation',
								match: /:/,
							},
							{
								type: 'command',
								match: /max-width|min-width/,
							},
							{
								type: 'condition',
								match: /and/,
							},
						],
					},
					{
						type: 'gap',
						pocket: 4,
					},
				],
			},
			{
				type: 'mixin',
				behind: /[\t ]*/,
				match: /(\.[a-zA-Z0-9_-]+)(\()(@+?)(\))(\s*)(\{)/, // в селекторе
				forward: /\n/,
				explode: [
					{
						type: 'mixin',
						pocket: 1,
					},
					{
						type: 'punctuation',
						pocket: 2,
					},
					{
						type: 'parameters',
						pocket: 3,
						inside: [
							{
								type: 'variable',
								match: /\$[a-zA-Z0-9_-]+/,
							},
							{
								type: 'default-value',
								match: /(:)(\s*)([a-zA-Z0-9_-]+)/,
								explode: [
									{
										type: 'punctuation',
										pocket: 1,
									},
									{
										type: '~',
										pocket: 2,
									},
									{
										type: '~',
										pocket: 3,
									},
								],
							},
							{
								type: 'punctuation',
								match: /,/,
							},
						],
					},
					{
						type: 'punctuation',
						pocket: 4,
					},
					{
						type: '~',
						pocket: 5,
					},
					{
						type: 'punctuation',
						pocket: 6,
					},
				]
			},
			{
				type: 'directive',
				match: /(@include|@each|@extend)/,
				behind: /[\s ]*/,
				forward: /\n/,
			},
			{
				type: 'label',
				match: /(!default|!global|!optional)/,
				forward: /;/,
			},
			{
				type: 'mixin',
				match: /\@[a-zA-Z0-9_-]+/, 
			},
			{
				type: 'variable',
				match: /\$[a-zA-Z0-9_-]+/,
			},
			{
				type: 'property',
				match: /([a-zA-Z-]+?)(\s*)(\+?_?:)(\s*)(.+?)(;)/,
				explode: [
					{
						type: 'name',
						pocket: 1,
					},
					{
						type: 'gap',
						pocket: 2,
					},
					{
						type: 'punctuation',
						pocket: 3,
					},
					{
						type: 'gap',
						pocket: 4,
					},
					{
						type: 'value',
						pocket: 5,
						inside: [
							{
								type: 'string',
								match: /('|").*?\1/,
							},
							{
								type: 'function',
								match: /[a-zA-Z0-9_-]+/,
								forward: /\(/,
							},
							{
								type: 'variable',
								match: /\$[a-zA-Z0-9_-]+/,
							},
						],
					},
					{
						type: 'punctuation',
						pocket: 6,
					},
				],
			},
			{
				type: 'selector',
				behind: /[\t ]*/,
				match: /.+\{/,
				forward: /\n/,
				inside: [
					{
						type: 'punctuation',
						match: /\{$/,
					},
					{
						type: 'merge',
						match: /[&]/,
					},
					{
						type: 'variable',
						match: /\$\{[a-zA-Z0-9_-]+\}/,
					},
					{
						type: 'punctuation',
						match: /[,+>~]/,
					},
					{
						type: 'bracket',
						match: /[()]/,
					},

					{
						type: 'attribute',
						match: /(\[)([a-z-]+)(\])/,
						explode: [
							{
								type: 'bracket',
								pocket: 1,
							},
							{
								type: 'name',
								pocket: 2,
							},
							{
								type: 'bracket',
								pocket: 3,
							},
						],
					},
					{
						type: 'attribute',
						match: /(\[)([a-z-]+)(\s*)([|$*~|^]?=)(\s*)(["'])([a-z-]+)(\6)(\])/,
						explode: [
							{
								type: 'bracket',
								pocket: 1,
							},
							{
								type: 'name',
								pocket: 2,
							},
							{
								type: 'gap',
								pocket: 3,
							},
							{
								type: 'operator',
								pocket: 4,
							},
							{
								type: 'gap',
								pocket: 5,
							},
							{
								type: 'quote',
								pocket: 6,
							},
							{
								type: 'value',
								pocket: 7,
							},
							{
								type: 'quote',
								pocket: 8,
							},
							{
								type: 'bracket',
								pocket: 9,
							},
						],
					},
					{
						type: 'function',
						match: /::?[a-z-]+/,
						forward: /\(/,
					},
					{
						type: 'pseudo',
						match: /::?[a-z-]+/,
						norward: /\(/,
					},
					{
						type: 'id',
						match: /#[a-z0-9_-]+/i,
					},
					{
						type: 'class',
						match: /\.[a-z0-9_-]+/i,
					},
				]
			},
			{
				type: 'bracket',
				match: /\{\}/,
			},
			
		];
		
		сommands.less = [
			{
				type: 'comment',
				match: /\/\/.*/,
			},
			{
				type: 'comment',
				match: /\/\*[\s\S]*?\*\//,
			},
			{
				type: 'command',
				match: /@(?:(?:-webkit-|-moz-|-o-)?keyframes|support)/,
			},
			{
				type: 'media',
				match: /(@media)(\s+)((?:\(.+?\)(?:\s+(?:and)\s)?)+)(\s*)/,
				behind: /[\t ]*/,
				forward: /\{/,
				explode: [
					{
						type: 'name',
						pocket: 1,
					},
					{
						type: 'gap',
						pocket: 2,
					},
					{
						type: '~',
						pocket: 3,
						inside: [
							{
								type: 'bracket',
								match: /[\(\)]/,
							},
							{
								type: 'punctuation',
								match: /:/,
							},
							{
								type: 'command',
								match: /max-width|min-width/,
							},
							{
								type: 'condition',
								match: /and/,
							},
						],
					},
					{
						type: 'gap',
						pocket: 4,
					},
				],
			},
			{
				type: 'mixin',
				behind: /[\t ]*/,
				match: /(\.[a-zA-Z0-9_-]+)(\()(.+?)(\))(\s*)(\{)/, // в селекторе
				forward: /\n/,
				explode: [
					{
						type: 'mixin',
						pocket: 1,
					},
					{
						type: 'punctuation',
						pocket: 2,
					},
					{
						type: 'parameters',
						pocket: 3,
						inside: [
							{
								type: 'variable',
								match: /@[a-zA-Z0-9_-]+/,
							},
							{
								type: 'default-value',
								match: /(:)(\s*)([a-zA-Z0-9_-]+)/,
								explode: [
									{
										type: 'punctuation',
										pocket: 1,
									},
									{
										type: '~',
										pocket: 2,
									},
									{
										type: '~',
										pocket: 3,
									},
								],
							},
							{
								type: 'punctuation',
								match: /,/,
							},
						],
					},
					{
						type: 'punctuation',
						pocket: 4,
					},
					{
						type: '~',
						pocket: 5,
					},
					{
						type: 'punctuation',
						pocket: 6,
					},
				]
			},
			/* пока оставим
			{
				type: 'namespace',
				match: /[#.][a-zA-Z0-9_-]+ >/,
				forward: /\s*\./,
			},
			*/
			
			
			{
				type: 'extend',
				match: /(&:extend)(\()(.+?)(\))/,
				forward: /;/,
				explode: [
					{
						type: 'command',
						pocket: 1,
					},
					{
						type: 'punctuation',
						pocket: 2,
					},
					{
						type: 'name',
						pocket: 3,
					},
					{
						type: 'punctuation',
						pocket: 4,
					},
				],
			},
			{
				type: 'mixin',
				match: /\.[a-zA-Z0-9_-]+/, // вставка
				forward: /[;(]/,
			},
			{
				type: 'variable',
				match: /@[a-zA-Z0-9_-]+/,
			},
			{
				type: 'property',
				match: /([a-zA-Z-]+?)(\s*)(\+?_?:)(\s*)(.+?)(;)/,
				explode: [
					{
						type: 'name',
						pocket: 1,
					},
					{
						type: 'gap',
						pocket: 2,
					},
					{
						type: 'punctuation',
						pocket: 3,
					},
					{
						type: 'gap',
						pocket: 4,
					},
					{
						type: 'value',
						pocket: 5,
						inside: [
							{
								type: 'string',
								match: /('|").*?\1/,
							},
							{
								type: 'function',
								match: /[a-zA-Z0-9_-]+/,
								forward: /\(/,
							},
							{
								type: 'variable',
								match: /@[a-zA-Z0-9_-]+/,
							},
						],
					},
					{
						type: 'punctuation',
						pocket: 6,
					},
				],
			},
			{
				type: 'selector',
				behind: /[\t ]*/,
				match: /.+\{/,
				forward: /\n/,
				inside: [
					{
						type: 'punctuation',
						match: /\{$/,
					},
					{
						type: 'merge',
						match: /[&]/,
					},
					{
						type: 'variable',
						match: /@\{[a-zA-Z0-9_-]+\}/,
					},
					{
						type: 'punctuation',
						match: /[,+>~]/,
					},
					{
						type: 'bracket',
						match: /[()]/,
					},
					{
						type: 'attribute',
						match: /(\[)([a-z-]+)(\])/,
						explode: [
							{
								type: 'bracket',
								pocket: 1,
							},
							{
								type: 'name',
								pocket: 2,
							},
							{
								type: 'bracket',
								pocket: 3,
							},
						],
					},
					{
						type: 'attribute',
						match: /(\[)([a-z-]+)(\s*)([|$*~|^]?=)(\s*)(["'])([a-z-]+)(\6)(\])/,
						explode: [
							{
								type: 'bracket',
								pocket: 1,
							},
							{
								type: 'name',
								pocket: 2,
							},
							{
								type: 'gap',
								pocket: 3,
							},
							{
								type: 'operator',
								pocket: 4,
							},
							{
								type: 'gap',
								pocket: 5,
							},
							{
								type: 'quote',
								pocket: 6,
							},
							{
								type: 'value',
								pocket: 7,
							},
							{
								type: 'quote',
								pocket: 8,
							},
							{
								type: 'bracket',
								pocket: 9,
							},
						],
					},
					{
						type: 'function',
						match: /::?[a-z-]+/,
						forward: /\(/,
					},
					{
						type: 'pseudo',
						match: /::?[a-z-]+/,
						norward: /\(/,
					},
					{
						type: 'id',
						match: /#[a-z0-9_-]+/i,
					},
					{
						type: 'class',
						match: /\.[a-z0-9_-]+/i,
					},
				]
			},
			{
				type: 'bracket',
				match: /\{\}/,
			},
			
		];

		сommands.javascript = [
			{
				type: 'marked',
				match: /\/\/!!.*/,
			},
			{
				type: 'comment',
				match: /\/\*[\s\S]*?\*\//,
			},
			{
				type: 'comment',
				match: /\/\/.*/,
			},
			{
				type: 'string',
				match: /('|"|`)\1/,
			},
			{
				type: 'string',
				match: /('|").*?[^\\]\1/,
				inside: [
					...inject.html,
				],
			},
			
			// Косые кавычки
				{
					type: 'string',
					match: /(`)([\s\S]*?[^\\])(`)/,
					
					explode: [
						{
							type: '~',
							pocket: 1,
						},
						{
							type: '~',
							pocket: 2,
							inside: [
								{
									type: 'insert',
									match: /(\$\{)([\s\S]*?)(\})/,
									explode: [
										{
											type: '~',
											pocket: 1,
										},
										{
											type: 'javascript',
											pocket: 2,
											mode: 'self',
										},
										{
											type: '~',
											pocket: 3,
										},
									],
								},
								...inject.html,
							],
							
						},
						{
							type: '~',
							pocket: 3,
						},
					]
					
				},
			//-
			// регулярки
				{
					type: 'regexp',
					match: /(\/)([^ ]*?)(\/)([a-z]*)/,
				
					explode: [
						{
							type: 'limiter',
							pocket: 1,
						},
						{
							type: 'regexp',
							pocket: 2,
						},
						{
							type: 'limiter',
							pocket: 3,
						},
						{
							type: 'modifier',
							pocket: 4,
						},
					]
				},
			//-
				
			{
				type: 'module-export',
				match: /\b(export)\b/,
			},
			{
				type: 'module-import',
				match: /\b(import)\b/,
			},
			{
				type: 'module-from',
				match: /\b(from)\b/,
			},
			{
				type: 'module-default',
				behind: /export\s/,
				match: /\b(default)\b/,
			},
			
			{
				type: 'async',
				match: /\b(async)\b/,
			},
			{
				type: 'await',
				match: /\b(await)\b/,
			},
			{
				type: 'keyword',
				match: /\b(if|else|elseif|switch|case|default|while|for|break|continue|return|in|of|class|instanceof|function|try|throw|catch|finally|typeof|yield)\b/,
			},
			{
				type: 'definition',
				match: /\b(var|let|const|new)\b/,
			},
			
			{
				type: 'window',
				match: /\b(window)\b/,
			},
			{
				type: 'document',
				match: /\b(document)\b/,
			},
			{
				type: 'console',
				match: /\b(console)\b/,
			},
			{
				type: 'this',
				match: /\b(this)\b/,
			},
			{
				type: 'value',
				match: /\b(true|false|null|undefined|Infinity|NaN)\b/,
			},
			{
				type: 'punctuation',
				match: /[,.:;]/,
			},
			{
				type: 'operator',
				match: /=|--?|\+\+?|\*|\/|!=?=?|<=?|>=?|===?|&&?|\|\|?|\?|~|\^|%/,
			},
			{
				type: 'bracket',
				match: /[\(\)\[\]\{\}]/,
			},
			{
				type: 'number',
				match: /\d+(\.\d+)?/,
			},
			{
				type: 'variable',
				nehind: /\./,
				match: /[_$a-zA-Z0-9]+/,
				norward: /[(.:]/,
			},
			{
				type: 'key',
				match: /[_$a-zA-Z0-9]+/,
				forward: / *:/,
			},
			{
				type: 'property',
				behind: /[^.]\./,
				match: /[_$a-zA-Z0-9]+/,
				norward: /\(/,
			},
			{
				type: 'object',
				match: /[_$a-zA-Z][_$a-zA-Z0-9]*/,
				forward: /\./,
			},
			{
				type: 'method',
				behind: /\./,
				match: /[_$a-zA-Z][_$a-zA-Z0-9]*/,
				forward: /\(/,
			},
			{
				type: 'function',
				nehind: /\./,
				match: /[_$a-zA-Z][_$a-zA-Z0-9]*/,
				forward: /\(/,
			},
			
		];
		
		сommands.jsx = [
			{
				type: 'tag',
				match: /<>|<\/>/,
			},
			{
				type: 'tag',
				match: /<\/?[a-zA-Z0-9-_]+/,
			},
			{
				type: 'tag',
				match: /\/>/,
			},
			{
				type: 'tag',
				nehind: /\s|=/,
				match: />/,
			},
			{
				type: 'attribute',
				//behind: /<[^>]*/,
				match: /[a-zA-Z0-9_-]+/,
				forward: /\s*=["'{]/,
			},
			
			...сommands.javascript,
		];
		
		сommands.typescript = [
			{
				type: 'keyword',
				match: /\b(interface|namespace|implements|enum|type)\b/,
			},
			{
				type: 'variable',
				match: /[a-zA-Z][a-zA-Z0-9_]*/,
				forward: /: [a-zA-Z][a-zA-Z0-9_]*/,
			},
			{
				type: 'type',
				behind: /: /,
				match: /[a-zA-Z][a-zA-Z0-9_]*(?:\s\|\s[a-zA-Z][a-zA-Z0-9_]*)*/,
			},
			{
				type: 'modifier',
				match: /\b(public|protected|private|static|readonly)\b/,
			},
			{
				type: 'abstract',
				match: /\b(abstract)\b/,
			},
			...сommands.javascript,
			
		];

		сommands.php = [
			{
				type: 'php-open',
				match: /%\?=|%\?php/,
			},
			{
				type: 'php-close',
				match: /\?%/,
			},
			
			{
				type: 'marked',
				match: /\/\/!!.*/,
			},
			{
				type: 'comment',
				match: /\/\*[\s\S]*?\*\//,
			},
			{
				type: 'comment',
				match: /(\/\/)(.*)/,
				
				explode: [
					{
						type: 'command',
						pocket: 1,
					},
					{
						type: 'text',
						pocket: 2,
					},
				]
			},
			
			/*
			{
				type: 'key',
				match: /'[_$a-zA-Z0-9]+'/,
				forward: /\s*=> /,
			},
			{
				type: 'key',
				match: /"[_$a-zA-Z0-9]+"/,
				forward: /\s*=> /,
			},
			{
				type: 'key',
				match: /[0-9]+/,
				forward: /\s*=> /,
			},
			{
				type: 'key',
				match: /'.+?'/,
				behind: /\[/,
				forward: /\]/,
			},
			*/
			
			// Строки
				{
					type: 'string',
					match: /''|""/,
				},
				{
					type: 'string',
					match: /'\\\\'/, // todo: более универсально сделать
				},
				{
					type: 'string',
					match: /'[\s\S]*?[^\\]'/,
					
					inside: [
						...inject.html,
						...inject.sql,
					],
				},
				{
					type: 'string',
					match: /"[\s\S]*?[^\\]"/,
					
					inside: [
						{
							type: 'variable',
							match: /\$[_a-zA-Z0-9]+/,
						},
						
						...inject.html,
						...inject.sql,
					],
				},
			//-
			
			{
				type: 'keyword',
				match: /\b(require_once|require|include_once|include|new|and|or|xor|array|echo|if|else|elseif|endif|switch|case|default|while|endwhile|for|endfor|foreach|endforeach|as|break|continue|return|class|interface|trait|namespace|use|extends|implements|instanceof|insteadof|function|try|throw|catch|finally)\b/,
			},
			{
				type: 'instance',
				match: /\b(\$this|parent|self)/,
			},
			{
				type: 'special',
				match: /\$_GET|\$_POST|\$_REQUEST|\$_SERVER|\$_SESSION|\$_COOKIE|\$GLOBALS/,
			},
			{
				type: 'modifier',
				match: /\b(public|protected|private|static)\b/,
			},
			{
				type: 'definition',
				match: /\b(const)\b/,
			},
			{
				type: 'global',
				match: /\b(global)\b/,
			},
			{
				type: 'abstract',
				match: /\b(abstract)\b/,
			},
			{
				type: 'value',
				match: /\b(true|false|null)\b/,
			},
			{
				type: 'punctuation',
				match: /[,.:;]/,
			},
			{
				type: 'operator',
				match: /=>|->|=|--?|\+\+?|\*|\/|!=?=?|<=?|>=?|===?|&&?|\|\|?|\?|~|\^|%/,
			},
			{
				type: 'bracket',
				match: /[\(\)\[\]\{\}]/,
			},
			{
				type: 'variable',
				match: /\$[_a-zA-Z0-9]+/,
				norward: /->/,
			},
			{
				type: 'object',
				match: /\$[_a-zA-Z][_a-zA-Z0-9]*/,
				forward: /->/,
			},
			{
				type: 'property',
				behind: /->/,
				match: /[_a-zA-Z0-9-]+/,
				norward: /\(/,
			},
			{
				type: 'method',
				behind: /->/,
				match: /[_a-zA-Z-][_a-zA-Z0-9-]*/,
				forward: /\(/,
			},
			{
				type: 'function',
				nehind: /->/,
				match: /[_a-zA-Z-][_a-zA-Z0-9-]*/,
				forward: /\(/,
			},
			{
				type: 'number',
				match: /\d+(\.\d+)?/,
			},
		];
		
		
		сommands.hbs = [
			{
				type: 'comment',
				match: /{\*[\s\S]*?\*}/,
			},
			{
				type: 'comment',
				match: /<!--[\s\S]*?-->/,
			},
			{
				type: 'tag',
				match: /(<style.*?>)([\s\S]*?)(<\/style>)/,
				explode: [
					{
						type: 'tag-name',
						pocket: 1,
					},
					{
						type: '~',
						pocket: 2,
						mode: 'css',
					},
					{
						type: 'tag-name',
						pocket: 3,
					},
				],
			},
			
			{
				type: 'tag',
				match: /(<script.*?>)([\s\S]*?)(<\/script>)/,
				explode: [
					{
						type: 'tag-name',
						pocket: 1,
					},
					{
						type: '~',
						pocket: 2,
						mode: 'javascript',
					},
					{
						type: 'tag-name',
						pocket: 3,
					},
				],
			},
			{
				type: 'tag-name',
				match: /<[^\/][^>\s]*?>/,
			},
			{
				type: 'tag-name',
				match: /<\/[^>\s]*?>/,
			},
			{
				type: 'tag',
				match: /(<[^\/][^>]*?)(\s+)([^>]*?)(\s*)(>)/,
				explode: [
					{
						type: 'tag-name',
						pocket: 1,
					},
					{
						type: 'gap',
						pocket: 2,
					},
					{
						type: 'attributes',
						pocket: 3,
						inside: [
							{
								type: 'attribute',
								nehind: /</,
								match: /(on[^\s]+?)(\s*)(=)(\s*)("|')([\s\S]*?)(\5)/,
								explode: [
									{
										type: 'name',
										pocket: 1,
									},
									{
										type: 'gap',
										pocket: 2,
									},
									{
										type: 'equal',
										pocket: 3,
									},
									{
										type: 'gap',
										pocket: 4,
									},
									{
										type: 'quote',
										pocket: 5,
									},
									{
										type: 'javascript',
										pocket: 6,
										mode: 'javascript',
									},
									{
										type: 'quote',
										pocket: 7,
									},
								],
							},
							{
								type: 'attribute',
								nehind: /</,
								match: /([^\s]+?)(\s*)(=)(\s*)("|')([\s\S]*?)(\5)/,
								explode: [
									{
										type: 'name',
										pocket: 1,
									},
									{
										type: 'gap',
										pocket: 2,
									},
									{
										type: 'equal',
										pocket: 3,
									},
									{
										type: 'gap',
										pocket: 4,
									},
									{
										type: 'quote',
										pocket: 5,
									},
									{
										type: 'value',
										pocket: 6,
										inside: [
											{
												type: 'command',
												match: /(\{\{)(.*?)(\}\})/,
												explode: [
													{
														type: 'bracket',
														pocket: 1,
													},
													{
														type: '~',
														pocket: 2,
														inside: [
															{
																type: 'variable',
																nehind: /\./,
																match: /[a-zA-Z0-9_]+/,
															},
															{
																type: 'property',
																behind: /\./,
																match: /[a-zA-Z0-9_]+/,
															},
														],
													},
													{
														type: 'bracket',
														pocket: 3,
													},
												],
											},
										],
									},
									{
										type: 'quote',
										pocket: 7,
									},
								],
							},
							{
								type: 'property',
								nehind: /</,
								match: /\b[^\s<>"']+?\b/,
							},
						],
					},
					{
						type: 'gap',
						pocket: 4,
					},
					{
						type: 'tag-name',
						pocket: 5,
					},
				],
			},
			{
				type: 'command',
				match: /(\{\{\}?)(.*?)(\}\}\}?)/,
				explode: [
					{
						type: 'bracket',
						pocket: 1,
					},
					{
						type: '~',
						pocket: 2,
				
						inside: [
							{
								type: 'keyword',
								match: /[#\/](?:each|if|with)/,
							},
							{
								type: 'variable',
								nehind: /\./,
								match: /[a-zA-Z0-9_]+/,
							},
							{
								type: 'property',
								behind: /\./,
								match: /[a-zA-Z0-9_]+/,
							},
							
						],
				
					},
					{
						type: 'bracket',
						pocket: 3,
					},
				],
			},
		];
		
		сommands.python = [
			{
				type: 'comment',
				match: /#.*/,
			},
			{
				type: 'string',
				match: /('''|""")\1/,
			},
			{
				type: 'string',
				match: /('|")\1/,
			},
			{
				type: 'string',
				match: /('''|""").*?[^\\]\1/,
				inside: [
					...inject.html,
				],
			},
			{
				type: 'string',
				match: /('|").*?[^\\]\1/,
				inside: [
					...inject.html,
				],
			},
			{
				type: 'keyword',
				match: /\b(if|else|elif|switch|case|while|for|break|continue|pass|return|in|is|def|class|try|raise|except|finally|typeof|yield|and|or|not|as|assert|del|from|global|lambda|from|import|with|nonlocal)\b/,
			},
			
			{
				type: 'async',
				match: /\b(async)\b/,
			},
			{
				type: 'await',
				match: /\b(await)\b/,
			},
			{
				type: 'value',
				match: /\b(True|False|None)\b/,
			},
			{
				type: 'punctuation',
				match: /[,.:;]/,
			},
			{
				type: 'operator',
				match: /=|-|\+|\*|\/|!=|<=?|>=?|==|%/,
			},
			{
				type: 'bracket',
				match: /[\(\)\[\]\{\}]/,
			},
			{
				type: 'number',
				match: /\d+(\.\d+)?/,
			},
			
			{
				type: 'method',
				behind: /\./,
				match: /[_$a-zA-Z][_$a-zA-Z0-9]*/,
				forward: /\(/,
			},
			{
				type: 'function',
				nehind: /\./,
				match: /[_$a-zA-Z][_$a-zA-Z0-9]*/,
				forward: /\(/,
			},
			
		];
		
		сommands.java = [
			{
				type: 'marked',
				match: /\/\/!!.*/,
			},
			{
				type: 'comment',
				match: /\/\*[\s\S]*?\*\//,
			},
			{
				type: 'comment',
				match: /\/\/.*/,
			},
			{
				type: 'string',
				match: /(""")\1/,
			},
			{
				type: 'string',
				match: /('|")\1/,
			},
			{
				type: 'string',
				match: /(''').*?[^\\]\1/,
				inside: [
					...inject.html,
				],
			},
			{
				type: 'string',
				match: /('|").*?[^\\]\1/,
				inside: [
					...inject.html,
				],
			},
			{
				type: 'type',
				match: /\b(byte|char|double|float|int|long|short|void|String)\b/,
			},
			{
				type: 'modifier',
				match: /\b(public|protected|private|static)\b/,
			},
			{
				type: 'definition',
				match: /\b(const)\b/,
			},
			{
				type: 'abstract',
				match: /\b(abstract)\b/,
			},
			{
				type: 'keyword',
				match: /\b(abstract|assert|boolean|break|case|catch|class|const|continue|default|do|else|enum|extends|final|finally|for|goto|if|implements|import|instanceof|interface|native|new|package|return|strictfp|super|switch|synchronized|this|throw|throws|transient|try|volatile|while|var)\b/,
			},
			
			{
				type: 'value',
				match: /\b(true|false|null)\b/,
			},
			{
				type: 'punctuation',
				match: /[,.:;]/,
			},
			{
				type: 'operator',
				match: /=|-|\+|\*|\/|!=|<=?|>=?|==|%/,
			},
			{
				type: 'bracket',
				match: /[\(\)\[\]\{\}]/,
			},
			{
				type: 'number',
				match: /\d+(\.\d+)?/,
			},
			
			{
				type: 'method',
				behind: /\./,
				match: /[_$a-zA-Z][_$a-zA-Z0-9]*/,
				forward: /\(/,
			},
			{
				type: 'function',
				nehind: /\./,
				match: /[_$a-zA-Z][_$a-zA-Z0-9]*/,
				forward: /\(/,
			},
			
		];
		сommands.cpp = [
			{
				type: 'marked',
				match: /\/\/!!.*/,
			},
			{
				type: 'comment',
				match: /\/\*[\s\S]*?\*\//,
			},
			{
				type: 'comment',
				match: /\/\/.*/,
			},
			{
				type: 'string',
				match: /(""")\1/,
			},
			{
				type: 'string',
				match: /('|")\1/,
			},
			{
				type: 'string',
				match: /('|").*?[^\\]\1/,
				inside: [
					...inject.html,
				],
			},
			{
				type: 'unsigned',
				match: /\b(unsigned)\b/,
			},
			{
				type: 'type',
				match: /\b(char|char8_tc|char16_t|char32_t|int|long|void|wchar_t|string|float)\b/,
			},
			{
				type: 'modifier',
				match: /\b(public|protected|private|static)\b/,
			},
			{
				type: 'definition',
				match: /\b(const)\b/,
			},
			{
				type: 'abstract',
				match: /\b(abstract)\b/,
			},
			{
				type: 'keyword',
				match: /\b(alignas|alignof|andB|and_eqB|asma|auto|bitandB|bitorB|bool|break|case|catch|class|complB|conceptc|const_cast|constevalc|constexpr|constinitc|continue|co_awaitc|co_returnc|co_yieldc|decltype|default|delete|do|double|dynamic_cast|else|enum|explicit|exportc|extern|false|for|friend|goto|if|inline|mutable|namespace|new|noexcept|notB|not_eqB|nullptr|operator|orB|or_eqB|register|reinterpret_cast|requiresc|return|short|signed|sizeof|static_assert|static_cast|struct|switch|template|this|thread_local|throw|try|typedef|typeid|typename|union|using|virtual|volatile|while|xorB|xor_eqB)\b/,
			},
			
			{
				type: 'value',
				match: /\b(true|false|null)\b/,
			},
			{
				type: 'punctuation',
				match: /[,.:;]/,
			},
			{
				type: 'operator',
				match: /=|-|\+|\*|\/|!=|<=?|>=?|==|%/,
			},
			{
				type: 'bracket',
				match: /[\(\)\[\]\{\}]/,
			},
			{
				type: 'number',
				match: /\d+(\.\d+)?/,
			},
			
			{
				type: 'method',
				behind: /\./,
				match: /[_$a-zA-Z][_$a-zA-Z0-9]*/,
				forward: /\(/,
			},
			{
				type: 'function',
				nehind: /\./,
				match: /[_$a-zA-Z][_$a-zA-Z0-9]*/,
				forward: /\(/,
			},
			
		];
		сommands.rust = [
			{
				type: 'marked',
				match: /\/\/!!.*/,
			},
			{
				type: 'comment',
				match: /\/\*[\s\S]*?\*\//,
			},
			{
				type: 'comment',
				match: /\/\/.*/,
			},
			{
				type: 'string',
				match: /(""")\1/,
			},
			{
				type: 'string',
				match: /('|")\1/,
			},
			{
				type: 'string',
				match: /('|").*?[^\\]\1/,
				inside: [
					...inject.html,
				],
			},
			{
				type: 'type',
				match: /\b(char|String|&str|bool|i8|u8|i16|u16|i32|u32|i64|u64|i128|u128|isize|usize|f32|f64)\b/,
			},
			{
				type: 'modifier',
				match: /\b(public|protected|private|static)\b/,
			},
			{
				type: 'definition',
				match: /\b(let|const|mut)\b/,
			},
			{
				type: 'abstract',
				match: /\b(abstract)\b/,
			},
			{
				type: 'keyword',
				match: /\b(as|async|await|break|const|continue|crate|dyn|else|enum|extern|false|fn|for|if|impl|in|loop|match|mod|move|pub|ref|return|Self|self|static|struct|super|trait|true|type|union|unsafe|use|where|while|abstract|become|box|do|final|macro|override|priv|try|typeof|unsized|virtual|yield)\b/,
			},
			
			{
				type: 'value',
				match: /\b(true|false|null)\b/,
			},
			{
				type: 'punctuation',
				match: /[,.:;]/,
			},
			{
				type: 'operator',
				match: /=|-|\+|\*|\/|!=|<=?|>=?|==|%/,
			},
			{
				type: 'bracket',
				match: /[\(\)\[\]\{\}]/,
			},
			{
				type: 'number',
				match: /\d+(\.\d+)?/,
			},
			
			{
				type: 'method',
				behind: /\./,
				match: /[_$a-zA-Z][_$a-zA-Z0-9]*/,
				forward: /\(/,
			},
			{
				type: 'function',
				nehind: /\./,
				match: /[_$a-zA-Z][_$a-zA-Z0-9]*/,
				forward: /\(/,
			},
			
		];
		
		сommands.terminal = [
			{
				type: 'keyword',
				match: /(sudo|php|npm|npx|yarn|composer|ssh|apt|nvm|wget|node)/,
				behind: /(?:\s|^)/,
				forward: /(?:\s|$)/,
			},
			{
				type: 'module',
				match: /(artisan)/,
				behind: /(?:\s|^)/,
				forward: /(?:\s|$)/,
			},
			{
				type: 'command',
				match: /(install|update|require|run|cd|pwd|mkdir|cat|ls)/,
				behind: /(?:\s|^)/,
				forward: /(?:\s|$)/,
			},
			{
				type: 'modifier',
				match: /--(.+?)(\s|$)/,
			},
			// todo: param с одним дефисом
		];
		сommands.htaccess = [
			
		];
		сommands.http = [
			
		];
		сommands.url = [
			
		];
		сommands.conf = [
			
		];
		сommands.text = [
			
		];
		
		return сommands;
	}

}



})({});
let oHigh = new cHigh();
let aeElem = document.getA('[⊸o="high"]');

for (let eElem of aeElem) {
	eElem.hext = oHigh.handle(eElem.hext, eElem.getD('╌m-lang'));
}
})({});
await (async (π)=>{
	let aeElem = document.getA('[⊸o="torc"]');

for (let eElem of aeElem) {
	eElem.hext = $.oTorc.trn(eElem.getD('╌m-kest'));
}

})({});
await (async (π)=>{
	let aeElem = document.getA('input');

for (let eElem of aeElem) {
	let vAttr = eElem.getR('autocomplete');
	
	if (vAttr != 'on') {
		eElem.setR('autocomplete', 'off');
	}
}

})({});
await (async (π)=>{
	
let iframes = document.getA('iframe[srcdoc]:n([style])');

for (let iframe of iframes) {
	iframe.addEventListener('load', function() {
		setFullHeight(iframe);
	});
	
	if (iframe.height === '0') {
		setFullHeight(iframe); // если загрузка раньше случилась
	}
	
	// solution - там релоад ифреймов по нажатию сделан
}

let timeoutId;
let pageWidth = document.documentElement.clientWidth;
window.addEventListener('resize', function() {
	if (pageWidth !== document.documentElement.clientWidth) {
		clearInterval(timeoutId);
		
		timeoutId = setTimeout(() => {
			for (let iframe of iframes) {
				setFullHeight(iframe);
			}
		}, 1000);
	}
	
	pageWidth = document.documentElement.clientWidth;
});

function setFullHeight(iframe) {
	let inner = iframe.contentWindow.document;
	
	let scrollHeight = Math.max(
		inner.body.scrollHeight, inner.documentElement.scrollHeight,
		inner.body.offsetHeight, inner.documentElement.offsetHeight,
		inner.body.clientHeight, inner.documentElement.clientHeight
	);
	
	let style = window.getComputedStyle(iframe);
	let fullHeight;
	
	if (style.boxSizing === 'border-box') {
		fullHeight = scrollHeight + parseInt(style.paddingTop) + parseInt(style.paddingBottom) + parseInt(style.borderTopWidth) + parseInt(style.borderBottomWidth);
	} else {
		fullHeight = scrollHeight;
	}
	
	if (+iframe.height !== fullHeight) {
		iframe.height = fullHeight;
	}
	
	iframe.height = +iframe.height + 5; // 5 эмпирически, тк возникала небольшая полоса прокрутки. Может с кодом выше что-то не то?
}
})({});






})({});
await (async (π)=>{
	await (async (π)=>{
	let aeWinn = document.getA('[╌w="bock/open"][╌m-type="W"]');
let aePage = document.getA('[╌w="bock/open"][╌m-type="P"]');

for (let eWinn of aeWinn) {
	let eLink = eWinn.getE('[╌e="link"]');
	
	eLink.addEventListener('click', function(event) {
		let vWinnWidth = window.outerWidth; // outer свойства не меняют значения при масштабировании страницы
		let vWinnHeight = window.outerHeight;
		
		let vHorShift = 100;
		let vVerShift = 130;
		
		let vLeft = window.screenX + vHorShift;
		let vTop  = window.screenY + vVerShift;
		
		let vWidth  = vWinnWidth  - 2 * vHorShift;
		let vHeight = vWinnHeight - 2 * vVerShift;
		
		let oDate = new Date();
		let oNewWin = window.open('about:blank', oDate.getTime(), 'left='+vLeft+',top='+vTop+',width='+vWidth+',height='+vHeight+',location=no');
		
		let vDoc = eWinn.getE('[╌e="code"]').getD('╌v-code');
		console.log(vDoc);
		oNewWin.document.write(vDoc);
		
		event.preventDefault();
	});
}
for (let ePage of aePage) {
	let eLink = ePage.getE('[╌e="link"]');
	
	eLink.addEventListener('click', function(event) {
		let vWinnWidth = window.innerWidth;
		let vWinnHeight = window.innerHeight;
		
		let vLeft = 0;
		let vTop  = 0;
		
		let vWidth  = screen.width;
		let vHeight = screen.height;
		
		let oDate = new Date();
		let oNewWin = window.open('about:blank', oDate.getTime(), 'left='+vLeft+',top='+vTop+',width='+vWidth+',height='+vHeight+',location=no,menubar=no');
		
		let vDoc = ePage.getE('[╌e="code"]').getD('╌v-code');
		oNewWin.document.write(vDoc);
		
		event.preventDefault();
	});
}




})({});
await (async (π)=>{
	
window.addEventListener('load', function() {
	let aeWigg = document.getA('[╌w="cont/shot"]');
	
	if (aeWigg.length > 0) {
		window.addEventListener('resize', function() {
			for (let eWigg of aeWigg) {
				let eImg = eWigg.getE('img');
				setInCenter(eWigg, eImg);
			}
		});
		
		for (let eWigg of aeWigg) {
			let eImg = eWigg.getE('img');
			setInCenter(eWigg, eImg);
			cropImage(eWigg, eImg);
			
			let aeArrow = eWigg.getA('[╌e="mark"][╌m-type="A"]');
			for (let eArrow of aeArrow) {
				let eCanv = document.createElement('canvas');
			
				let nHeig = 30;
				let nWidt = +eArrow.getD('╌nL');
				eCanv.height = nHeig;
				eCanv.width  = nWidt;
				
				eCanv.style.left = +eArrow.getD('╌nX') + 'px';
				eCanv.style.top  = +eArrow.getD('╌nY') - nHeig / 2 + 'px'; 
				
				eCanv.style.transform = 'rotate(' + eArrow.getD('╌nA') + 'deg)';
				
				eWigg.append(eCanv);
				
				let oCtx = eCanv.getContext('2d');
				oCtx.strokeStyle = 'red';
				oCtx.fillStyle = 'red';
				oCtx.lineWidth = 5;
				
				drawArrow(oCtx, nWidt, nHeig);
			}
			
			let aeText = eWigg.getA('[╌e="mark"][╌m-type="T"]');
			for (let eText of aeText) {
				eText.style.left = eText.getD('╌nX') + 'px';
				eText.style.top  = eText.getD('╌nY') + 'px';
			}
			
			let aeRect = eWigg.getA('[╌e="mark"][╌m-type="R"]');
			for (let eRect of aeRect) {
				eRect.style.width  = eRect.getD('╌nW') + 'px';
				eRect.style.height = eRect.getD('╌nH') + 'px';
				eRect.style.left   = eRect.getD('╌nX') + 'px';
				eRect.style.top    = eRect.getD('╌nY') + 'px'; 
			}
		}
		
		function drawArrow(oCtx, nWidt, nHeig) {
			oCtx.beginPath();
			oCtx.moveTo(10, nHeig / 2);
			oCtx.lineTo(nWidt, nHeig / 2);
			oCtx.stroke();
			
			oCtx.beginPath();
			oCtx.moveTo(0, nHeig / 2);
			oCtx.lineTo(40, 3);
			oCtx.lineTo(30, nHeig / 2);
			oCtx.lineTo(40, nHeig - 3);
			oCtx.lineTo(0, nHeig / 2);
			oCtx.fill();
			
		}
		
		function setInCenter(eWigg, eImg) {
			let nCent;
			
			if (eImg.hasD('╌nC')) {
				nCent = +eImg.getD('╌nC');
			} else {
				let aeArrow = eWigg.getA('[╌e="mark"][╌m-type="A"]');
				
				if (aeArrow.length == 1) {
					nCent = +aeArrow[0].getD('╌nX');
				} else {
					nCent = 0;
				}
			}
			
			let nCentX = nCent - eWigg.offsetWidth / 2;
			if (nCentX > 0) {
				eWigg.scrollLeft = nCentX;
			}
		}
		
		function cropImage(eWigg, eImg) {
			if (eImg.hasD('╌knCr')) {
				let anPoint = eImg.getD('╌knCr').split(':');
				
				if (anPoint.length == 1) {
					anPoint[1] = eWigg.scrollHeight;
				}
				
				let nScrollLineSize = 15;
				eWigg.style.height = (anPoint[1] - anPoint[0] + nScrollLineSize) + 'px';
				eWigg.scrollTop = anPoint[0];
				
				eWigg.setD('╌m-crop', 'T');
			}
		}
	}
});


})({});
await (async (π)=>{
	let aeWigg = document.getA('[╌w="cont/task"]');

if (aeWigg.length > 0) {
	let vLesh = document.body.getD('⋯v-lesh');
	
	let i = 1;

	for (let eWigg of aeWigg) {
		let eHead = document.crtE('<p ╌e="head"></p>'); // todo h4
		eWigg.prepend(eHead);
		
		let eTnum = document.crtE('<span ╌e="tnum">№' + i + '</span>');
		eHead.prepend(eTnum);
		
		eTnum.addEventListener('click', function() {
			h.copyToClipBoard(this.getP('~v-text'));
		});
		
		if (vLesh) {
			let eTash = document.crtE('<span ╌e="tash">' + vLesh + '</span>');
			eHead.append(eTash);
			
			eTash.addEventListener('click', function() {
				h.copyToClipBoard(vLesh);
			});
			eWigg.setP('~v-id', i);
		}
		
		i++;
	}
}

if (aeWigg.length > 0) {
	for (let eWigg of aeWigg) {
		let aePar = eWigg.getA('[╌t="p"]');
		
		if (aePar.length === 1) {
			let ePar = aePar[0];
			let nLeng = ePar.getP('~v-text').length;
			
			if (nLeng <= 100) {
				ePar.setD('╌m-type', 'S');
			}
		}
	}
}

})({});
await (async (π)=>{
	let aeWigg = document.getA('[╌w="cont/teor"]');

for (let eWigg of aeWigg) {
	let vHext = eWigg.exrP('~v-hext');
	
	let eHead = document.crtE('<p ╌e="head" ╌z="p">' + $.oTorc.trn('study-theory-on-those-links') + ':</p>');
	let eHext = document.crtE('<p ╌e="linr" ╌z="p">' + vHext + '</p>');
	
	eWigg.append(eHead);
	eWigg.append(eHext);
}

})({});
await (async (π)=>{
	let eMenu = document.getE('[╌w="menu/pane"]');

if (eMenu) {
	let aeLink = eMenu.getA('a');
	
	await (async (π)=>{
		// Нормализатор меню для off версии
	
	for (let eLink of aeLink) {
		let qHref = clear(eLink.getR('href'));
		eLink.setD('╌q-href', qHref);
	}
	
	// наверное надо при сборке всем ссылкам data-q-href - начальное значение
	function clear(qHref) {
		if ($.uqC.Ṫ === 'F') {
			return qHref.replace(/^(\.\.\/)+/, '/').replace(/\.html/, '/');
		} else {
			return qHref;
		}
	}
	})({});
	await (async (π)=>{
		let mMode = eMenu.getD('╌m-mode');
	
	if (mMode === 'P') {
		for (let eLink of aeLink) {
			eLink.hext = document.conH(`
				<span ╌e="coun"></span>
				<span ╌e="text">${eLink.hext}</span>
			`);
		}
	}
	if (mMode === 'G') {
		
		for (let eLink of aeLink) {
			let eGerm = eLink.getE('[╌e="germ"]');
			eGerm.remove();
			
			eLink.hext = document.conH(`
				<span ╌e="coun"></span>
				<span ╌e="text">${eLink.hext}</span>
			`);
			
			eLink.append(eGerm);
		}
	}
	
	if (mMode === 'H') {
		let mBook = eMenu.getD('╌m-book');
		let aeSect = eMenu.getA('[╌m-sect]');
		
		for (let eSect of aeSect) {
			let mSect = eSect.getD('╌m-sect');
			
			let aeLink = eSect.getA('a');
			
			for (let eLink of aeLink) {
				let mLess = eLink.getD('╌m-less');
				let mHash = mBook + mSect + mLess;
				
				eLink.hext = document.conH(`
					<span ╌e="coun"></span>
					<span ╌e="text">${eLink.hext}</span>
					<span ╌e="hash">${mHash}</span>
				`);
				
				let eTodo = eLink.getE('[≁s="apet"], [≁s="crit"]');
				if (eTodo) {
					eLink.append(eTodo);
				}
			}
		}
	}
	if (mMode === 'T') {
		// нормализация ссылок
			let mHype  = eMenu.getD('╌m-hype', 'N'); // N,Q
			
			for (let eLink of aeLink) {
				let vHead = eLink.getD('╌v-head');
				
				if (!vHead) {
					let qHref = eLink.getD('╌q-href');
					
					let oMach = qHref.match(/\/([^\/]+?)\/?$/);
					
					if (oMach && oMach[1]) {
						if (mHype == 'N') {
							vHead = oMach[1];
						}
						
						if (mHype == 'Q') {
							vHead = oMach[1].replace('-', ' ').toUpperCase();
						}
					}
				}
				
				eLink.hext =  document.conH(`
					<span ╌e="head" ╌m-hype="${mHype}">${vHead}</span>
					<span ╌e="desc">${eLink.hext}</span>`
				);
			}
		//-
		// алфавитный порядок
			let vCler = eMenu.getD('╌v-cler', ''); // очистка типа oc_
			
			let uaeLink = {
				a: [], b: [], c: [], d: [], e: [], f: [], g: [],
				h: [], i: [], j: [], k: [], l: [], m: [], n: [],
				o: [], p: [], q: [], r: [], s: [], t: [], u: [],
				v: [], w: [], x: [], y: [], z: [],
			};
			for (let eLink of aeLink) {
				let qHref = eLink.getD('╌q-href');
				let vName = clear(qHref);
				
				if (vCler) {
					vName = vName.replace(vCler, '');
				}
			
				if (!uaeLink[ vName[0] ]) {
					uaeLink[ vName[0] ] = []; // на случай если начало не с буквы
				}
				
				uaeLink[ vName[0] ].push(eLink);
			}
			
			let ePane = document.crtE('<section ╌e="pane" ╌m-curr="F" ╌m-tabb="a-z" ╌m-type="R"></section>');
			//section.classList.add('sorted');
			
			for (let vLett in uaeLink) {
				if (uaeLink[vLett].length > 0) {
					let h2 = document.createElement('h2');
					h2.hext = vLett.toUpperCase();
					ePane.append(h2);
					
					let eSect = document.createElement('div');
					ePane.append(eSect);
					
					for (let eLink of uaeLink[vLett]) {
						eSect.append(eLink.cloneNode(true));
					}
				}
			}
			eMenu.prepend(ePane);
			
			function clear(qHref) {
				let vName = qHref.match(/\/([^/]+)\/$/)[1].toLowerCase();
				
				if (vName.indexOf('.') == -1) {
					return vName;
				} else {
					return vName.match(/\.([^.]+)$/)[1];
				}
			}
		//-
		// блок управления вкладками
			let eBabr = document.crtE(`<div ╌w="menu/babr"></div>`);
			eMenu.insertAdjacentElement('beforebegin', eBabr);
			
			let oTabr = new $.cTabr;
			
			let aePane = eMenu.getA('[╌e="pane"]');
			
			for (let ePane of aePane) {
				let mType = ePane.getD('╌m-type');
				let mTabb = ePane.getD('╌m-tabb');
				let eBage = document.crtE(`<div ╌e="bage" ╌m-curr="F" ╌m-type="${mType}">${mTabb}</div>`);
				eBabr.append(eBage);
				
				oTabr.addT(mTabb, new cYell([ePane, eBage]));
				
				eBage.on('click', function() {
					oTabr.setC(mTabb);
				});
			}
			
			oTabr.setC('a-z');
		//-
	}
	
	})({});
	
	await (async (π)=>{
		let aeLink = eMenu.getA('a[╌m-fixt="T"]');
	
	for (let eLink of aeLink) {
		let eHead = eLink.getE('[╌e="head"]');
		
		if (eHead) {
			eHead.setD('╌m-hype', 'T');
		}
	}
	
	})({});
	await (async (π)=>{
		let aeLink = eMenu.getA('a[╌v-pref], a[╌v-post]');
	
	for (let eLink of aeLink) {
		let eHead = eLink.getE('[╌e="head"]');
		
		if (eHead) {
			let vPref = eLink.getD('╌v-pref', '');
			let vPost = eLink.getD('╌v-post', '');
			
			eHead.hext = vPref + eHead.hext + vPost;
		}
	}
	
	})({});
	
	await (async (π)=>{
		// Ссылка с теста
	/*
		/?p=Bs:Ru,Nm;Cl;Lp;
		Lp - последний без уроков, после него все далее будут
	*/
	
	let kkkmLess = $.uqC.uṼ['p'];
	
	if (kkkmLess) {
		let mLast; // last sect
		let uamLess = {};
		let akkmLess = kkkmLess.replace(/;$/, '').split(';');
		
		let i = 0;
		for (let kkmLess of akkmLess) {
			let [mSect, kmLess] = kkmLess.split(':');
			uamLess[mSect] = [];
			
			if (kmLess) {
				let amLess = kmLess.split(',');
				uamLess[mSect].push(...amLess);
			}
			
			i++;
			
			if (i === akkmLess.length) {
				mLast = mSect;
			}
		}
		
		let isFuth = false;
		let aeSect = eMenu.getA('[╌m-sect]');
		
		for (let eSect of aeSect) {
			let mSect = eSect.getD('╌m-sect');
			
			let aeLess = eSect.getA('a');
			
			for (let eLess of aeLess) {
				if (!isFuth) {
					if (uamLess[mSect]) {
						if (uamLess[mSect].length > 0) {
							let mLess = eLess.getD('╌m-less');
							
							if (uamLess[mSect].includes(mLess)) {
								eLess.setD('╌m-stud', 'T');
							} else {
								eLess.setD('╌m-stud', 'F');
							}
						} else {
							eLess.setD('╌m-stud', 'T');
						}
					} else {
						eLess.setD('╌m-stud', 'F');
					}
				} else {
					eLess.setD('╌m-stud', 'T');
				}
			}
			
			if (mSect === mLast) {
				isFuth = true;
			}
		}
	}
	})({});
}

})({});
await (async (π)=>{
	let eWigg = document.getE('[╌w="nict/logo"]');

if (eWigg) {
	// todo: это в класс работы с датами
	function addZero(nNum) {
		if (nNum <= 9) {
			nNum = '0' + nNum;
		}
		
		return nNum;
	}
	
	let date = new Date();
	let time = addZero(date.getHours()) + ':' + addZero(date.getMinutes());
	let day = date.getDay();
	
	let vName;
	if (day != 0 && day != 6) {
		if (time <= '09.00' || time >= '22.00') {
			vName = 'sleep';
		} else if ((time >= '10.00' && time <= '11.00') || (time >= '14.00' && time <= '15.00')) {
			vName = 'break';
		} else if (time >= '17.00' && time <= '22.00') {
			vName = 'relax';
		} else {
			vName = 'job';
		}
	} else {
		vName = 'holiday';
	}
	
	let eImg = eWigg.getE('[╌e="img"]');
	eImg.src = '/tore/wigg/nict/logo/@/' + vName + '.png';
}

})({});
await (async (π)=>{
	let eWigg = document.getE('[╌w="nict/mainmenu"]');

if (eWigg) {
	let qHurrP = $.uqC.P;
	
	let eBack = document.crtE('<div ╌e="back" ⋯m-acte="F"><span>&larr;</span></div>');
	eWigg.prepend(eBack);
	
	let eHead = document.crtE('<div ╌e="head"></div>');
	eWigg.prepend(eHead);
	
	let eMain  = eWigg.getE('[╌e="main"]');
	let aeOpen = eWigg.getA('[╌e="open"]');
	
	eBack.addEventListener('click', function(event) {
		let eActe = eWigg.getE('[╌e="subb"][⋯m-acte="T"]');
		
		if (eActe) {
			eActe.setD('⋯m-acte', 'F');
		}
		
		eHead.setD('⋯m-acte', 'F');
		eBack.setD('⋯m-acte', 'F');
		eMain.setD('⋯m-acte', 'T');
	});
	
	aeOpen.sort(function(eA, eB) {
		let vA = eA.getD('╌q-href');
		let vB = eB.getD('╌q-href');
		
		if (!vA || !vB || vA.length <= vB.length) {
			return 1;
		} else {
			return -1;
		}
	});
	
	let isFound = false;
	for (let eOpen of aeOpen) {
		eOpen.addEventListener('click', function(event) {
			let mTarg = eOpen.getD('╌m-targ');
			let eTarg = eWigg.getE('[╌e="subb"][╌m-tabb="' + mTarg + '"]');
			
			if (eTarg) {
				eMain.setD('⋯m-acte', 'F');
				eTarg.setD('⋯m-acte', 'T');
				eHead.setD('⋯m-acte', 'T');
				eBack.setD('⋯m-acte', 'T');
				
				eHead.setP('~v-hext', eOpen.hext + ':');
			}
		});
		
		// curr
		let qHrefP = eOpen.getD('╌q-href');
		
		if (!isFound && qHrefP && qHrefP != '' && qHurrP.startsWith(qHrefP)) {
			eOpen.setD('╌c', 'curr');
			
			isFound = true;
			// break; не нужен!
		}
	}
	
	let aeLink = eWigg.getA('[╌e="subb"] a');
	
	for (let eLink of aeLink) {
		let qHref = eLink.getAttribute('href'); // обязательно через getAttribute
		
		// проверить, работает ли для off
		qHref = qHref.replace(/^(\.\.\/)+/g, '/').replace(/\.html$/, ''); // для off
		
		if (qHref != '' && qHurrP.startsWith(qHref)) {
			eLink.setD('╌c', 'curr');
		}
	}
}


})({});
await (async (π)=>{
	let eWigg = document.getE('[╌w="nict/over"]');

if (eWigg) {
	let eHash = eWigg.getE('[╌e="hash"]');
	
	if (eHash) {
		let vLesh = eHash.text;
		
		eHash.addEventListener('click', function() {
			h.copyToClipBoard(vLesh);
		});
	}
}
})({});
await (async (π)=>{
	let eWigg = document.getE('[╌w="nict/them"]');

if (eWigg) {
	let aeSich = eWigg.getA('[╌e="sich"]');
	
	for (let eSich of aeSich) {
		let mType = eSich.getD('╌m-type');
		
		eSich.on('click', function() {
			document.body.setD('⋯q', mType);
			$.oCokr.set('--q', mType, {'max-age': 3600 * 24 * 365 * 20});
		});
	}
}

})({});



})({});




})({})