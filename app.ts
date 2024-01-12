// app.ts
// Ensure you have TypeScript installed: npm install -g typescript
// Compile TypeScript to JavaScript: tsc app.ts

// Define a simple interface for the API response
interface ApiResponse {
    city: string;
    temperature: number;
    units: string;
}

// Function to fetch data from the API
async function fetchData(endpoint: string): Promise<{ data: ApiResponse, time: number }> {
    const startTime = new Date().getTime();
    const response = await fetch(endpoint);
    const data: ApiResponse = await response.json();
    const endTime = new Date().getTime();
    const timeTaken = endTime - startTime;
    return { data, time: timeTaken };
}

// Function to render data on the HTML page as a table row
function renderData(dataWithTime: { data: ApiResponse; time: number }) {
    const appElement = document.getElementById('appTable');
    if (appElement) {
        const rowElement = document.createElement('tr');
        rowElement.innerHTML = `
            <td>${dataWithTime.data.city}</td>
            <td>${dataWithTime.data.temperature}°</td>
            <td>${dataWithTime.time}ms</td>
        `;
        appElement.appendChild(rowElement);
    }
}



// Entry point
async function main() {
    console.log('Main function executed');
    try {
        const endpoints = [
            '/temperature?city=San Francisco',
            '/temperature?city=San Francisco&units=imperial',
            '/temperature?city=New York',
            '/temperature?city=New York&units=imperial',
            '/temperature?city=Dallas',
            '/temperature?city=Dallas&units=imperial',
            '/temperature?city=Chicago',
            '/temperature?city=Chicago&units=imperial',
            '/temperature?city=London',
            '/temperature?city=London&units=imperial',
            '/temperature?city=Hong Kong',
            '/temperature?city=Hong Kong&units=imperial',
            '/temperature?city=Bangalore',
            '/temperature?city=Bangalore&units=imperial',
            '/temperature?city=Philadelphia',
            '/temperature?city=Philadelphia&units=imperial',
            '/temperature?city=Paris',
            '/temperature?city=Paris&units=imperial',
            '/temperature?city=Charlotte',
            '/temperature?city=Charlotte&units=imperial',
            '/temperature?city=Denver',
            '/temperature?city=Denver&units=imperial',
            '/temperature?city=Austin',
            '/temperature?city=Austin&units=imperial',
            // Add more endpoints as needed
        ];

        // Fetch data for each endpoint
        for (const endpoint of endpoints) {
            const apiDataWithTime = await fetchData(endpoint);
            renderData(apiDataWithTime);
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Run the main function when the DOM is ready
document.addEventListener('DOMContentLoaded', main);
