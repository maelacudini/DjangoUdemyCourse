const parallax = ( el, speed = 0.2 ) => {
  if ( !el ) return

  let frameRequested = false

  const updatePosition = () => {
    el.style.transform = `translateY(${window.scrollY * speed}px)`
    frameRequested = false
  }

  const requestUpdate = () => {
    if ( frameRequested ) return

    frameRequested = true
    window.requestAnimationFrame( updatePosition )
  }

  updatePosition()
  window.addEventListener( 'scroll', requestUpdate, { passive: true } )
}

parallax( document.getElementById( 'hero-image' ) )