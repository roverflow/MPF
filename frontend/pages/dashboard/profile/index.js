import Head from "next/head";
import Link from "next/link";
import Layout from "@/layouts/Layout";
import styles from "@/styles/Home.module.css";
import Cookies from "js-cookie";
import { useRouter } from "next/router";

const Profile = () => {
  const router = useRouter();
  const logout = () => {
    Cookies.remove("logged_in");
    Cookies.remove("access_token");
    Cookies.remove("refresh_token");
    router.push("/auth/signin");
  };
  return (
    <>
      <Head>
        <title>MPF</title>
        <meta name="description" content="Missing Person Finder" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/aams.svg" />
      </Head>
      <Layout>
        <main className={styles.auth_lt}>
          <div className={styles.description}>
            <p>
              Check your&nbsp;
              <code className={styles.code}>Profile</code>
            </p>
            <div>
              <Link href="/about">
                By <code className={styles.code}>Team Threshold</code>
              </Link>
            </div>
          </div>
          <div className={styles.authx}>
            <button
              className="btn-primary"
              onClick={logout}
              style={{ padding: "1rem", borderRadius: "0.5rem" }}
            >
              Logout
            </button>
          </div>
        </main>
      </Layout>
    </>
  );
};

export default Profile;
