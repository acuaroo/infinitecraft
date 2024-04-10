export const dynamic = "force-dynamic"

export async function GET(request: Request) {
  const sendURL: string = request.url.split("?murl=")[1];
  const requestURL: string = sendURL.split("&headers=")[0];

  const encodedHeaders: string | null = new URL(sendURL).searchParams.get("headers");
  const parsedHeaders: Headers = new Headers(JSON.parse(decodeURIComponent(encodedHeaders || "")));

  // send a get request to requestURL using parsdeHeaders
  const response: Response = await fetch(requestURL, {
    headers: parsedHeaders,
  });

  const data: any = await response.json();

  return new Response(JSON.stringify(data), {
    headers: { "Content-Type": "application/json" },
  });
}