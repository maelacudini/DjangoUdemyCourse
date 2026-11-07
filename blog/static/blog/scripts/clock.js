function updateClock() {
  const now = new Date();

  let hours = now.getHours();
  let minutes = now.getMinutes();

  hours = String( hours ).padStart( 2, '0' );
  minutes = String( minutes ).padStart( 2, '0' );

  const currentTime = `UDINE (IT), ${hours}:${minutes}`;

  document.getElementById( 'clock' ).textContent = currentTime;
}

updateClock();
setInterval( updateClock, 60000 );