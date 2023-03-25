import Head from "next/head";
import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/router";
import { Inter } from "next/font/google";
import styles from "@/styles/Home.module.css";
import axios from "axios";
import Cookies from "js-cookie";
import Layout from "@/layouts/Layout";

const inter = Inter({ subsets: ["latin"] });

export default function SignIn() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(false);

  const router = useRouter();

  const handleSubmit = () => {
    axios
      .post("http://localhost:8000/api/auth/login", { email, password })
      .then((res) => {
        if (res.data.status === "success") {
          Cookies.set("logged_in", true);
          Cookies.set("access_token", res.data.access_token);
          Cookies.set("refresh_token", res.data.refresh_token);
          router.push("/");
        } else {
          console.log(res.data);
        }
      })
      .catch((err) => {
        console.log(err);
        setError(true);
      });
  };

  return (
    <>
      <Head>
        <title>MPF</title>
        <meta
          name="description"
          content="Automatic Attendence Management System"
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/aams.svg" />
      </Head>
      <Layout>
        <main className={styles.auth_lt}>
          <div className={styles.description}>
            <p>
              <code className={styles.code}>Sign in</code>&nbsp;to your account
            </p>
            <div>
              <Link href="/about">
                By <code className={styles.code}>Team Threshold</code>
              </Link>
            </div>
          </div>

          <div className={styles.authx}>
            <form
              className="d-flex flex-column gap-3"
              style={{ width: "500px" }}
            >
              <div className="d-flex flex-column gap-2">
                <label className={styles.code}>Email</label>
                <input
                  onChange={(e) => setEmail(e.target.value)}
                  type="email"
                  name="email"
                  id="email"
                  className={styles.code}
                />
              </div>
              <div className="d-flex flex-column gap-2">
                <label className={styles.code}>Password</label>
                <input
                  onChange={(e) => setPassword(e.target.value)}
                  type="password"
                  name="password"
                  id="password"
                  className={styles.code}
                />
              </div>
              <div
                className={styles.btn_base}
                type="submit"
                onClick={handleSubmit}
              >
                <p>Sign in</p>
              </div>
            </form>

            <div
              className="position-fixed bottom-0 end-0 p-3"
              style={{ zIndex: "11" }}
            >
              <div
                className={`${styles.code} text-danger ${error ? "" : "toast"}`}
              >
                <div className={`toast-header`}>
                  <strong className="me-auto">Error</strong>
                  <button
                    type="button"
                    className="btn-close"
                    data-bs-dismiss="toast"
                    aria-label="Close"
                    onClick={() => setError(false)}
                  ></button>
                </div>
                <div className="toast-body">
                  Please check your username or password
                </div>
              </div>
            </div>
          </div>
        </main>
      </Layout>
    </>
  );
}
