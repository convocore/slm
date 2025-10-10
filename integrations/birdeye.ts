/**
 * Minimal Birdeye metadata lookup used by the interpreter.
 * This proof-of-concept only fetches basic token information.
 */

export async function fetchTokenSnapshot(address: string) {
  const headers = {
    accept: "application/json",
    "x-chain": "solana",
    "X-API-KEY": process.env.BIRDEYE_KEY || ""
  };

  const url = `https://public-api.birdeye.so/defi/v3/token/meta-data/single?address=${address}`;

  try {
    const response = await fetch(url, { headers });
    const json = await response.json();

    if (!json || !json.success || !json.data) {
      return { ok: false, reason: "Birdeye did not return metadata" };
    }

    const data = json.data;

    return {
      ok: true,
      name: data.name || null,
      symbol: data.symbol || null,
      logo: data.logo_uri || null,
      links: data.extensions || {}
    };
  } catch (err) {
    return { ok: false, reason: "Network or parsing error" };
  }
}
