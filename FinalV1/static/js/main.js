(() => {
	const hand = document.querySelector('.hand');
	const leaflet = document.querySelector('.leaflet');
	const pageElems = document.querySelectorAll('.page');
	let pageCount = 0;
	let currentMenu;

	const handPos = {x: 0, y: 0};
	const targetPos = {x: 0, y: 0};
	let distX;
	let distY;

	function getTarget(elem, className) {
		while (!elem.classList.contains(className)) {
			elem = elem.parentNode;

			if (elem.nodeName == 'BODY') {
				elem = null;
				return;
			}
		}

		return elem;
	}

	function closeLeaflet() {
		pageCount = 0;
		document.body.classList.remove('leaflet-opened');
		pageElems[2].classList.remove('page-flipped');
		setTimeout(() => {
			pageElems[0].classList.remove('page-flipped');
		}, 500);
	}

	function zoomIn(elem) {
		const rect = elem.getBoundingClientRect();
		const dx = window.innerWidth/2 - (rect.x + rect.width/2);
		const dy = window.innerHeight/2 - (rect.y + rect.height/2);
		let angle;

		switch (elem.parentNode.parentNode.parentNode.dataset.page*1) {
			case 1:
				angle = -30;
				break;
			case 2:
				angle = 0;
				break;
			case 3:
				angle = 30;
				break;
		}

		document.body.classList.add('zoom-in');
		leaflet.style.transform = `translate3d(${dx}px, ${dy}px, 50vw) rotateY(${angle}deg)`;
		currentMenu = elem;
		currentMenu.classList.add('current-menu');
	}

	function zoomOut() {
		leaflet.style.transform = 'translate3d(0, 0, 0)';
		if (currentMenu) {
			document.body.classList.remove('zoom-in');
			currentMenu.classList.remove('current-menu');
			currentMenu = null;
		}
	}

	function render() {
		distX = targetPos.x - handPos.x;
		distY = targetPos.y - handPos.y;
		handPos.x = handPos.x + distX*0.1;
		handPos.y = handPos.y + distY*0.1;
		hand.style.transform = `translate(${handPos.x-60}px, ${handPos.y+30}px)`;
		requestAnimationFrame(render);
	}

	render();

	leaflet.addEventListener('click', e => {
		let pageElem = getTarget(e.target, 'page');
		
		if (pageElem) {
			pageElem.classList.add('page-flipped');
			pageCount++;

			if (pageCount == 2) {
				document.body.classList.add('leaflet-opened');
			}
		}

		let closeBtnElem = getTarget(e.target, 'close-btn');
		if (closeBtnElem) {
			closeLeaflet();
			zoomOut();
		}

		let menuItemElem = getTarget(e.target, 'menu-item');
		if (menuItemElem) {

			if (!document.body.classList.contains('zoom-in')) {
				zoomIn(menuItemElem);
			}
		}

		let backBtn = getTarget(e.target, 'back-btn');
		if (backBtn) {
			zoomOut();
		}
	});

	leaflet.addEventListener('animationend', () => {
		leaflet.style.animation = 'none';
	});

	window.addEventListener('mousemove', e => {
		targetPos.x = e.clientX - window.innerWidth*0.7;
		targetPos.y = e.clientY - window.innerHeight*0.7;
	});
})();