import React, { useEffect } from "react";
import Cookies from "js-cookie";
import { useRouter } from "next/router";

const Layout = (props) => {
  const router = useRouter();
  useEffect(() => {
    const log = Cookies.get("logged_in");
    if (log === "true") {
      console.log("cool");
    } else {
      router.push("/auth/signin");
    }
    if (router.pathname == "/auth/signin") {
      if (log == "true") {
        router.push("/");
      }
    }
  }, []);
  return <>{props.children}</>;
};

export default Layout;
