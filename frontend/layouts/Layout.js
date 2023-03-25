import React, { useEffect, useState } from "react";
import Cookies from "js-cookie";
import { useRouter } from "next/router";

const Layout = (props) => {
  const router = useRouter();
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    const log = Cookies.get("logged_in");
    if (log === "true") {
      setLoading(false);
    } else {
      router.push("/auth/signin");
      setLoading(false);
    }
    if (router.pathname == "/auth/signin") {
      if (log == "true") {
        router.push("/");
        setLoading(false);
      }
    }
  }, []);
  if (loading) {
    return (
      <div
        style={{ display: "flex", height: "100vh", justifyContent: "Center" }}
      >
        <div class="spinner-border" role="status">
          <span class="sr-only">.</span>
        </div>
      </div>
    );
  }
  return <>{props.children}</>;
};

export default Layout;
