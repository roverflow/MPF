import Head from "next/head";
import { useState } from "react";
import Link from "next/link";
import { Inter } from "next/font/google";
import styles from "@/styles/Home.module.css";
import axios from "axios";

const inter = Inter({ subsets: ["latin"] });

export default function SignIn() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = () => {
    axios
      .post("http://localhost:8000/api/auth/login", { email, password })
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <>
      <Head>
        <title>AAMS</title>
        <meta
          name="description"
          content="Automatic Attendence Management System"
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/aams.svg" />
      </Head>
      <main className={styles.auth_lt}>
        <div className={styles.description}>
          <p>
            <code className={styles.code}>Sign in</code>&nbsp;to your account
          </p>
          <div>
            <Link href="/about">
              By <code className={styles.code}>Team AAMS</code>
            </Link>
          </div>
        </div>

        <div className={styles.auth}>
          <form className="d-flex flex-column gap-3" style={{ width: "500px" }}>
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
        </div>

        <div className="d-flex">
          <Link href="/auth/signup" className={styles.card}>
            <h2 className={inter.className}>SignUp</h2>
            <p className={inter.className}>Already have an account?</p>
          </Link>
        </div>
      </main>
    </>
  );
}
