/**
 * Minimal WebSocket listener for Helius transaction streams.
 * This listens for token balance changes on a specific mint address.
 *
 * This is a proof-of-concept for how real-time data integrates
 * into the agent workflow. No frontend bindings are included.
 */

export function listenToToken(
  address: string,
  onEvent: (evt: { type: "buy" | "sell"; amount: number; ts: number }) => void
) {
  const apiKey = process.env.HELIUS_KEY || "";
  const wsUrl = `wss://mainnet.helius-rpc.com/?api-key=${apiKey}`;

  const ws = new WebSocket(wsUrl);

  ws.onopen = () => {
    ws.send(
      JSON.stringify({
        jsonrpc: "2.0",
        id: 1,
        method: "transactionSubscribe",
        params: [
          { vote: false, accountInclude: [address] },
          { commitment: "confirmed" }
        ]
      })
    );
  };

  ws.onmessage = (event) => {
    try {
      const msg = JSON.parse(event.data);
      const tx = msg?.params?.result;
      if (!tx) return;

      const pre = tx.meta?.preTokenBalances?.find(
        (b: any) => b.mint === address
      );
      const post = tx.meta?.postTokenBalances?.find(
        (b: any) => b.mint === address
      );

      if (!pre || !post) return;

      const delta =
        post.uiTokenAmount.uiAmount -
        pre.uiTokenAmount.uiAmount;

      if (delta === 0) return;

      onEvent({
        type: delta > 0 ? "buy" : "sell",
        amount: Math.abs(delta),
        ts: Date.now()
      });
    } catch {
      // ignore malformed messages
    }
  };

  return () => {
    ws.close();
  };
}
