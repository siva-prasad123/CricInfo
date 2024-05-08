// frontend/public/app.js
document.addEventListener('DOMContentLoaded', function() {
    fetch('/.netlify/functions/get_tournaments')
        .then(response => response.json())
        .then(data => {
            const tournamentsDiv = document.getElementById('tournaments');
            for (const tournamentName in data) {
                tournamentsDiv.innerHTML += `<h1>${tournamentName}</h1>`;
                const matches = data[tournamentName].matches;
                matches.forEach(match => {
                    tournamentsDiv.innerHTML += `
                        <div class="match">
                            <h2>Match ID: ${match.match_id}</h2>
                            <p><strong>Pitch Report:</strong> ${match.pitch_report}</p>
                            <p><strong>Toss Status:</strong> ${match.toss_status}</p>
                            <p><strong>Current Players:</strong> ${match.current_players.join(', ')}</p>
                            <p><strong>Bowler:</strong> ${match.bowler}</p>
                            <p><strong>Target:</strong> ${match.target}</p>
                        </div>
                    `;
                });
            }
        })
        .catch(error => console.error('Error fetching tournament data:', error));
});
