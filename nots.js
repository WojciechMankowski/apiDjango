// Przykładowe dane, które chcesz wysłać do API
const placeData = {
  name: "Nowe Miejsce",
  address: "Przykładowa ulica 123",
  // Dodaj więcej pól zgodnie z modelem Place w Twoim API
};

// Funkcja do wysyłania żądania POST do API
function addNewPlace(placeData) {
  // Ustawienia żądania
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(placeData) // Konwersja danych miejsca na format JSON
  };

  // Wykonanie żądania do API
  fetch('http://localhost:8000/api/places/', requestOptions)
    .then(response => {
      if (!response.ok) {
        // Obsługa odpowiedzi z błędem od serwera
        throw new Error('Network response was not ok');
      }
      return response.json(); // Parsowanie odpowiedzi JSON
    })
    .then(data => {
      console.log(data); // Logowanie odpowiedzi z serwera (np. potwierdzenie dodania miejsca)
    })
    .catch(error => {
      console.error('There was a problem with your fetch operation:', error);
    });
}

// Wywołanie funkcji z przykładowymi danymi
addNewPlace(placeData);
