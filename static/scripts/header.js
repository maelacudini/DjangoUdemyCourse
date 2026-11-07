const header = document.getElementById( 'header' )
// const headerSpacer = document.getElementById( 'header-spacer' )

if ( header ) {
  let prevScrollPos = window.pageYOffset
  let headerHasFocus = false
  const headerHeight = header.offsetHeight

  const showHeader = () => {
    header.style.top = '0'
  }

  header.addEventListener( 'focusin', () => {
    headerHasFocus = true
    showHeader()
  } )

  header.addEventListener( 'focusout', ( event ) => {
    if ( !header.contains( event.relatedTarget ) ) {
      headerHasFocus = false
    }
  } )

  // headerSpacer.style.height = headerHeight + 'px'

  const toggleHeaderPosition = () => {
    const currentScrollPos = window.pageYOffset

    if ( headerHasFocus || prevScrollPos > currentScrollPos ) {
      showHeader()
    } else {
      header.style.top = `-${headerHeight}px`
    }

    prevScrollPos = currentScrollPos
  }

  window.addEventListener( 'scroll', toggleHeaderPosition, { passive: true } )
}