## Demo in browser

First, update Chroma's config to allow the `localhost:3000` origin for CORS.

For example, you could start Chroma with

```bash
CHROMA_SERVER_CORS_ALLOW_ORIGINS='["http://localhost:3000"]' chroma run
```

Then, in this folder:

1. `pnpm i`
2. `pnpm dev`
3. visit `localhost:3000`

## Running and Hosting the Application

To run and host the application, follow these steps:

1. Ensure you have Node.js and pnpm installed on your machine.
2. Clone the repository and navigate to the `clients/js/examples/browser` directory.
3. Install the dependencies by running `pnpm i`.
4. Start the development server by running `pnpm dev`.
5. Open your browser and visit `http://localhost:3000` to access the application.

## Uploading Files and Storing in Vector DB

The application allows you to upload files from the browser and store them in the vector database. Follow these steps:

1. Open the application in your browser.
2. Use the file input element to select a file for upload.
3. The file content will be read and stored in the vector database.

## Retrieval Process

The application also demonstrates the retrieval process from the vector database. You can query the stored files and documents using the search functionality provided in the UI.

## Credits

This application was created by Maluchuru Sai Dinesh Reddy.
