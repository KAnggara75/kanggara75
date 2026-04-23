import http from "k6/http";

const hostUrl = "https://profile-counter.glitch.me/KAnggara75/count.svg";
export default function () {
	http.get(hostUrl);
}

export const options = {
	vus: 100,
	duration: "10s",
};
