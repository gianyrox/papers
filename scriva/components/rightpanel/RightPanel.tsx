"use client";

import ChatPanel from "./ChatPanel";

export default function RightPanel() {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        height: "100%",
        fontFamily: "var(--font-inter), system-ui, sans-serif",
      }}
    >
      <ChatPanel />
    </div>
  );
}
