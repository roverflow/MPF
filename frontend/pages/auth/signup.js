import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import { Inter } from "next/font/google";
import styles from "@/styles/Home.module.css";

const inter = Inter({ subsets: ["latin"] });

export default function SignUp() {
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
            Create your&nbsp;
            <code className={styles.code}>Student account</code>
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
                type="email"
                name="email"
                id="email"
                className={styles.code}
              />
            </div>
            <div className="d-flex flex-column gap-2">
              <label className={styles.code}>Password</label>
              <input
                type="password"
                name="password"
                id="password"
                className={styles.code}
              />
            </div>
            <div className="d-flex flex-column gap-2">
              <label className={styles.code}>Confirm Password</label>
              <input
                type="password"
                name="cpassword"
                id="cpassword"
                className={styles.code}
              />
            </div>
            <div className={styles.btn_base}>
              <p>Sign Up</p>
            </div>
          </form>
        </div>

        <div className="d-flex">
          <Link href="/auth/signin" className={styles.card}>
            <h2 className={inter.className}>SignIn</h2>
            <p className={inter.className}>Already have an account?</p>
          </Link>
        </div>
      </main>
    </>
  );
}
