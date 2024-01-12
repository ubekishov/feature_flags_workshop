"use strict";
// app.ts
// Ensure you have TypeScript installed: npm install -g typescript
// Compile TypeScript to JavaScript: tsc app.ts
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
// Function to fetch data from the API
function fetchData(endpoint) {
    return __awaiter(this, void 0, void 0, function* () {
        const startTime = new Date().getTime();
        const response = yield fetch(endpoint);
        const data = yield response.json();
        const endTime = new Date().getTime();
        const timeTaken = endTime - startTime;
        return { data, time: timeTaken };
    });
}
// Function to render data on the HTML page as a table row
function renderData(dataWithTime) {
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
function main() {
    return __awaiter(this, void 0, void 0, function* () {
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
                const apiDataWithTime = yield fetchData(endpoint);
                renderData(apiDataWithTime);
            }
        }
        catch (error) {
            console.error('Error fetching data:', error);
        }
    });
}
// Run the main function when the DOM is ready
document.addEventListener('DOMContentLoaded', main);
