// lambda code that upon request, takes the &headers= query parameter, turns those into headers, removes it from the url, and sends the request to the url with the headers

import * as https from "node:https";

export const handler = (event) => {
  const url = event.url;
  const headers = JSON.parse(event.headers);

  const options = {
    method: "GET",
    headers: headers,
  };

  return new Promise((resolve, reject) => {
    const req = https.request(url, options, (res) => {
      let data = "";
      res.on("data", (chunk) => {
        data += chunk;
      });
      res.on("end", () => {
        resolve({
          statusCode: 200,
          body: data,
        });
      });
    });

    req.on("error", (error) => {
      reject({
        statusCode: 500,
        body: error,
      });
    });

    req.end();
  });
};